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
    on_transaction_loaded_signal = pyqtSignal(dict)

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

        # Connect model signals to controller slots
        self._model.transactions_loaded_signal.connect(
            self.on_transaction_loaded)

        # Connect controller signals to view slots
        self.on_transaction_loaded_signal.connect(
            self._main_view.display_transactions)

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

    @pyqtSlot(dict)
    def on_transaction_loaded(self, data):
        """Handle transaction loaded signal.

        When a signal from the model is received to confirm the user's
        transactions have been loaded, signals the view to display the
        transactions.

        Args:
            loaded (bool): whether the transactions have been loaded
        """
        self.on_transaction_loaded_signal.emit(data)
