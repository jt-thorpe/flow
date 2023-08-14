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
    request_view_initialise_total_label_signal = pyqtSignal(float, float)

    def __init__(self, model, view):
        """Initialize MainViewController.

        Args:
            model (FlowModel): the model
            view (MainAppView): the main window view
        """
        super().__init__()

        self._model = model
        self._main_view = view
        self._main_view._ui.income_table.setModel(
            self._model._income_transaction_data)
        self._main_view._ui.income_table.setColumnHidden(0, True)
        self._main_view._ui.income_table.setColumnHidden(1, True)
        self._main_view._ui.income_table.setColumnHidden(5, True)
        self._main_view._ui.expense_table.setModel(
            self._model._expense_transaction_data)
        self._main_view._ui.expense_table.setColumnHidden(0, True)
        self._main_view._ui.expense_table.setColumnHidden(1, True)
        self._main_view._ui.expense_table.setColumnHidden(5, True)

    def set_up_connections(self):
        """Set up connections.
        
        Connects all signals and slots.
        """
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
        self.request_view_initialise_total_label_signal.connect(
            self._main_view.initialise_total_labels)

        # Connect model signals to controller slots
        self._model.load_pie_chart_signal.connect(
            self._main_view._ui.pie_chart.update_data)
        self._model.update_labels_signal.connect(
            self.initialise_view_total_labels)

    def clean_up_connections(self):
        """Clean up connections.
        
        Disconnects all signals and slots.
        """
        # Disconnect view signals to controller slots
        self._main_view.main_view_loaded_signal.disconnect(
            self.on_main_view_loaded)
        self._main_view.add_income_btn_clicked_signal.disconnect(
            self.add_transaction_signal_received)

        # Disconnect controller signals to model slots
        self.request_load_user_transactions_signal.disconnect(
            self._model.initialise_user_transactions)
        self.request_add_transaction_signal.disconnect(
            self._model.add_transaction_to_db)

        # Disconnect controller signals to view slots
        self.on_transaction_loaded_signal.disconnect(
            self._main_view.display_transactions)
        self.request_view_initialise_total_label_signal.disconnect(
            self._main_view.initialise_total_labels)

        # Disconnect model signals to controller slots
        self._model.load_pie_chart_signal.disconnect(
            self._main_view._ui.pie_chart.update_data)
        self._model.update_labels_signal.disconnect(
            self.initialise_view_total_labels)

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

    @pyqtSlot(float, float)
    def initialise_view_total_labels(self, income, expense):
        """Update the total labels in the view.

        Args:
            income (float): the total income
            expenses (float): the total expenses
        """
        self.request_view_initialise_total_label_signal.emit(income, expense)
        
