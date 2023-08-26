from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QDateTime
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QSizePolicy
from models.transaction_model import Income, Expense, Transaction
from views.main_tabs_ui import Ui_main_tabs_window
from resources.widgets.pie_chart_widget import PieChartWidget


class MainAppView(QMainWindow):
    """MainApp view."""
    main_view_loaded_signal = pyqtSignal(bool)
    add_income_btn_clicked_signal = pyqtSignal(Transaction)
    add_expense_btn_clicked_signal = pyqtSignal(Transaction)

    def __init__(self):
        """Initialize MainApp view."""
        super().__init__()

        self._ui = Ui_main_tabs_window()
        self._ui.setupUi(self)

        self._ui.tab_bar.setCurrentIndex(1)  # set to dashboard tab

        self._ui.income_date_edit.setDateTime(
            QDateTime.currentDateTime().toPyDateTime())
        self._ui.income_date_edit.setDisplayFormat("dd/MM/yyyy")

        self._ui.expense_date_edit.setDateTime(
            QDateTime.currentDateTime().toPyDateTime())
        self._ui.expense_date_edit.setDisplayFormat("dd/MM/yyyy")

        self._ui.pie_chart = PieChartWidget()
        self._ui.pie_chart.setParent(self._ui.pie_chart_frame)
        self._ui.pie_chart.setSizePolicy(QSizePolicy.Policy.Expanding,
                                         QSizePolicy.Policy.Expanding)

        self._ui.pie_chart_frame.setLayout(QVBoxLayout())
        self._ui.pie_chart_frame.layout().addWidget(self._ui.pie_chart.canvas)

    def set_up_connections(self):
        """Connect widgets to view methods."""
        self._ui.add_income_btn.clicked.connect(
            self.add_income_btn_clicked)
        self._ui.add_expense_button.clicked.connect(
            self.add_expense_btn_clicked)

    def clean_up_connections(self):
        """Disconnect widgets from view methods."""
        self._ui.add_income_btn.clicked.disconnect(
            self.add_income_or_expense_btn_clicked)
        self._ui.add_expense_button.clicked.disconnect(
            self.add_income_or_expense_btn_clicked)

    def notify_view_loaded(self):
        """Emit main_view_loaded_signal to controller."""
        self.main_view_loaded_signal.emit(True)

    @pyqtSlot(dict)
    def add_transactions_to_view(self, data):
        """Display transactions in the view.

        Args:
            data (dict): the user's transactions
        """
        for item in data:
            self.transaction_data.add_transaction(item)

    @pyqtSlot(float, float)
    def update_piechart_data(self, income, expense):
        """Update the pie chart.

        Args:
            income (float): total income
            expense (float): total expense
        """
        self._ui.pie_chart.update_data(income, expense)

    @pyqtSlot(float, float)
    def update_total_labels(self, income, expense):
        """Update the total and lts labels.

        Args:
            income (float): total income
            expense (float): total expense
        """
        self._ui.total_income.setText(f"{income:.2f}")
        self._ui.total_expense.setText(f"{expense:.2f}")
        self._ui.left_to_spend.setText(f"{income - expense:.2f}")

    def add_income_btn_clicked(self):
        """Handle add income button clicked signal."""
        # TODO: implement tags
        amount = self._ui.income_amount_line_edit.text()
        if amount == "":
            self.display_field_error()
            return
        new_income = Income(None,
                            None,
                            amount,
                            self._ui.income_date_edit.date().toPyDate(),  # yyyy-mm-dd here to match db
                            self._ui.income_description_text_edit.toPlainText()
                            )
        print(new_income.get_date())
        self.add_income_btn_clicked_signal.emit(new_income)
        self._ui.income_amount_line_edit.clear()
        self._ui.income_description_text_edit.clear()

    def add_expense_btn_clicked(self):
        """Handle add expense button clicked signal."""
        # TODO: implement tags
        amount = self._ui.expense_amount_line_edit.text()
        if amount == "":
            self.display_field_error()
            return
        new_expense = Expense(None,
                              None,
                              amount,
                              self._ui.expense_date_edit.date().toPyDate(),  # yyyy-mm-dd here to match db
                              self._ui.expense_description_text_edit.toPlainText()
                              )
        self.add_expense_btn_clicked_signal.emit(new_expense)
        self._ui.expense_amount_line_edit.clear()
        self._ui.expense_description_text_edit.clear()

    def display_field_error(self):
        """Display an error message for a missing field."""
        message_box = QMessageBox()
        message_box.setWindowTitle("Missing Field")
        message_box.setText("Please enter an amount.")
        message_box.exec()
        if self._ui.tab_bar.currentIndex() == 0:
            self._ui.income_amount_line_edit.setFocus()
        else:
            self._ui.expense_amount_line_edit.setFocus()
