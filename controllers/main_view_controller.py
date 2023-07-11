from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class MainViewController(QObject):
    """Main view controller.

    Handles the main window view. Receives signals from the view and sends
    signals to the model.

    Attributes:
        model (FlowModel): the model
        view (MainAppView): the main window view
    """

    def __init__(self, model, view):
        """Initialize MainViewController.

        Args:
            model (FlowModel): the model
            view (MainAppView): the main window view
        """
        super().__init__()

        self._model = model
        self._view = view
