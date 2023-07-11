from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class MainViewController(QObject):
    """Main view controller.

    Handles the main window view. Receives signals from the view and sends
    signals to the model.

    Attributes:
        model (FlowModel): the model
        view (MainAppView): the main window view
    """

    request_load_user_transactions_signal = pyqtSignal(bool)

    def __init__(self, model, view):
        """Initialize MainViewController.

        Args:
            model (FlowModel): the model
            view (MainAppView): the main window view
        """
        super().__init__()

        self._model = model
        self._main_view = view

        # Connect view signals to controller slots
        self._main_view.main_view_loaded_signal.connect(
            self.on_main_view_loaded)

        # Connect controller signals to model slots
        self.request_load_user_transactions_signal.connect(
            self._model.load_user_transactions)

    @pyqtSlot(bool)
    def on_main_view_loaded(self, loaded):
        """Handle main view loaded signal.

        When a signal from the view is received to confirm it has been loaded,
        signals the model to load the user's transactions.

        Args:
            is_authenticated (bool): whether the user is authenticated
        """
        if loaded:
            self.request_load_user_transactions_signal.emit(True)
