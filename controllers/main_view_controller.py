from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class MainViewController(QObject):
    """Main view controller.

    Handles the main window view. Receives signals from the view and sends
    signals to the model.

    Attributes:
        _model (FlowModel): the model
        _view (MainAppView): the main window view
    """
    request_load_user_transactions_signal = pyqtSignal(bool)
    on_transaction_loaded_signal = pyqtSignal(dict)
    request_add_transaction_signal = pyqtSignal(dict)

    def __init__(self, model, view):
        """Initialize MainViewController.

        Args:
            model (FlowModel): the model
            view (MainAppView): the main window view
        """
        super().__init__()

        self._model = model
        self._main_view = view

    def set_up_connections(self):
        # Connect view signals to controller slots
        self._main_view.main_view_loaded_signal.connect(
            self.on_main_view_loaded)
        self._main_view.add_income_btn_clicked_signal.connect(
            self.add_transaction_signal_received)
        
        # Connect controller signals to model slots
        self.request_load_user_transactions_signal.connect(
            self._model.load_user_transactions)
        self.request_add_transaction_signal.connect(
            self._model.add_transaction_to_db)
        
        # Connect model signals to controller slots
        self._model.transactions_loaded_signal.connect(
            self.on_transaction_loaded)
        
        # Connect controller signals to view slots
        self.on_transaction_loaded_signal.connect(
            self._main_view.display_transactions)
        
    def clean_up_connections(self):
        """Clean up connections."""
        # Disconnect view signals from controller slots
        self._main_view.main_view_loaded_signal.disconnect(
            self.on_main_view_loaded)
        self._main_view.add_income_btn_clicked_signal.disconnect(
            self.add_transaction_signal_received)
        
        # Disconnect controller signals from model slots
        self.request_load_user_transactions_signal.disconnect(
            self._model.load_user_transactions)
        self.request_add_transaction_signal.disconnect(
            self._model.add_transaction)
        
        # Disconnect model signals from controller slots
        self._model.transactions_loaded_signal.disconnect(
            self.on_transaction_loaded)
        
        # Disconnect controller signals from view slots
        self.on_transaction_loaded_signal.disconnect(
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

        When a signal from the model is received that the user's transactions
        have been loaded, signals the view to display the transactions.

        Args:
            data (dict): the user's transactions
        """
        self.on_transaction_loaded_signal.emit(data)

    @pyqtSlot(dict)
    def add_transaction_signal_received(self, new_income):
        """Handle add income signal.

        When a signal from the view is received to add income, signals the
        model to add the income to the database.

        Args:
            data (dict): the income data
        """
        if new_income is not None:
            self.request_add_transaction_signal.emit(new_income)
