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
        self._main_view._ui.income_table.setModel(self._model._income_transaction_data)
        self._main_view._ui.income_table.setColumnHidden(0, True)
        self._main_view._ui.income_table.setColumnHidden(1, True)
        self._main_view._ui.income_table.setColumnHidden(5, True)
        self._main_view._ui.expense_table.setModel(self._model._expense_transaction_data)
        self._main_view._ui.expense_table.setColumnHidden(0, True)
        self._main_view._ui.expense_table.setColumnHidden(1, True)
        self._main_view._ui.expense_table.setColumnHidden(5, True)

    def set_up_connections(self):
        # Connect view signals to controller slots
        self._main_view.main_view_loaded_signal.connect(
            self.on_main_view_loaded)
        self._main_view.add_income_btn_clicked_signal.connect(
            self.add_transaction_signal_received)
        
        # Connect controller signals to model slots
        self.request_load_user_transactions_signal.connect(
            self._model.initialise_user_transactions)
        self.request_add_transaction_signal.connect(
            self._model.add_transaction_to_db)
        
        # Connect controller signals to view slots
        self.on_transaction_loaded_signal.connect(
            self._main_view.display_transactions)
        
        # Connect model signals to controller slots
        self._model.load_pie_chart_signal.connect(
            self._main_view._ui.pie_chart.update_data)
        
    def clean_up_connections(self):
        # Disconnect view signals from controller slots
        self._main_view.main_view_loaded_signal.disconnect(
            self.on_main_view_loaded)
        self._main_view.add_income_btn_clicked_signal.disconnect(
            self.add_transaction_signal_received)
        
        # Disconnect controller signals from model slots
        self.request_load_user_transactions_signal.disconnect(
            self._model.load_user_transactions)
        self.request_add_transaction_signal.disconnect(
            self._model.add_transaction_to_db)
        
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
    def add_transaction_signal_received(self, new_transaction):
        """Handle add income signal.

        Calls the model to first add the transaction to the database,
        then the model.

        Args:
            data (dict): the income data
        """
        if new_transaction["is_income"]:
            self._model._income_transaction_data.add_transaction(
                self._model.add_transaction_to_db(new_transaction)
                )
        else:
            self._model._expense_transaction_data.add_transaction(
                self._model.add_transaction_to_db(new_transaction)
                )
        
        