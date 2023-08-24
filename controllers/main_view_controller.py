from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from models.transaction_model import Expense, Transaction


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
    request_model_add_transaction_signal = pyqtSignal(Transaction)
    request_view_piechart_change_signal = pyqtSignal(float, float)
    request_view_label_change_signal = pyqtSignal(float, float)

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
            self._model._income_data)
        self._main_view._ui.expense_table.setModel(
            self._model._expense_data)

    def set_up_connections(self):
        """Set up connections.

        Connects all signals and slots.
        """
        # Model -> Controller -> View
        # Connect model signals to controller slots
        self._model.model_totals_changed_signal.connect(
            self.on_model_totals_changed)

        # Connect controller signals to view slots
        self.on_transaction_loaded_signal.connect(
            self._main_view.add_transactions_to_view)

        self.request_view_piechart_change_signal.connect(
            self._main_view.update_piechart_data)
        self.request_view_label_change_signal.connect(
            self._main_view.update_total_labels)

        # View -> Controller -> Model
        # Connect view signals to controller slots
        self._main_view.main_view_loaded_signal.connect(
            self.on_main_view_loaded)

        self._main_view.add_income_btn_clicked_signal.connect(
            self.on_add_transaction_clicked)
        self._main_view.add_expense_btn_clicked_signal.connect(
            self.on_add_transaction_clicked)

        # Connect controller signals to model slots
        self.request_load_user_transactions_signal.connect(
            self._model.initialise_user_transactions)

        self.request_model_add_transaction_signal.connect(
            self._model.add_transaction)

    def clean_up_connections(self):
        """Clean up connections.

        Disconnects all signals and slots.
        """
        # Model -> Controller -> View
        # Disconnect model signals from controller slots
        self._model.model_totals_changed_signal.disconnect(
            self.on_model_totals_changed)

        # Disconnect controller signals from view slots
        self.on_transaction_loaded_signal.disconnect(
            self._main_view.add_transactions_to_view)

        self.request_view_piechart_change_signal.disconnect(
            self._main_view.update_piechart_data)
        self.request_view_label_change_signal.disconnect(
            self._main_view.update_total_labels)

        # View -> Controller -> Model
        # Disconnect view signals from controller slots
        self._main_view.main_view_loaded_signal.disconnect(
            self.on_main_view_loaded)

        self._main_view.add_income_btn_clicked_signal.disconnect(
            self.on_add_transaction_clicked)
        self._main_view.add_expense_btn_clicked_signal.disconnect(
            self.on_add_transaction_clicked)

        # Disconnect controller signals from model slots
        self.request_load_user_transactions_signal.disconnect(
            self._model.initialise_user_transactions)

        self.request_model_add_transaction_signal.disconnect(
            self._model.add_transaction)

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

    @pyqtSlot(Transaction)
    def on_add_transaction_clicked(self, transaction):
        """Handle add transaction signal.

        When a signal from the view is received to add a transaction, signals
        the model to add the transaction to the database.

        Args:
            transaction (Transaction): the new transaction
        """
        self.request_model_add_transaction_signal.emit(transaction)

    @pyqtSlot(float, float)
    def on_model_totals_changed(self, income, expense):
        """Update the pie chart in the view.

        Args:
            income (float): the total income
            expenses (float): the total expenses
        """
        self.request_view_piechart_change_signal.emit(income, expense)
        self.request_view_label_change_signal.emit(income, expense)

    @pyqtSlot(float, float)
    def request_view_update_label(self, income, expense):
        """Update the total labels in the view.

        Args:
            income (float): the total income
            expenses (float): the total expenses
        """
        self.request_view_update_labels_signal.emit(income, expense)
