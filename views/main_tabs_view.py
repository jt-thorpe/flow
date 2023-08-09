from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QDateTime, QRect
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout

from views.main_tabs_ui import Ui_main_tabs_window
from views.semi_circle_pie_chart import SemiCirclePieChartWidget


class MainAppView(QMainWindow):
    """MainApp view."""
    main_view_loaded_signal = pyqtSignal(bool)
    add_income_btn_clicked_signal = pyqtSignal(dict)

    def __init__(self):
        """Initialize MainApp view."""
        super().__init__()

        self._ui = Ui_main_tabs_window()
        self._ui.setupUi(self)
        self._ui.tab_bar.setCurrentIndex(1)  # set to dashboard tab
        self._ui.income_date_edit.setDateTime(QDateTime.currentDateTime().toPyDateTime())
        self._ui.expense_date_edit.setDateTime(QDateTime.currentDateTime().toPyDateTime())

        self._ui.pie_chart = SemiCirclePieChartWidget()
        self._ui.pie_chart.setParent(self._ui.dashboard_tab)
        self._ui.pie_chart.ax.set_facecolor('none')

    def set_up_connections(self):
        """Set up connections."""
        # TODO: standardise button names
        self._ui.add_income_btn.clicked.connect(self.add_income_or_expense_btn_clicked)
        self._ui.add_expense_button.clicked.connect(self.add_income_or_expense_btn_clicked)

    def clean_up_connections(self):
        """Clean up connections."""
        self._ui.add_income_btn.clicked.disconnect(self.add_income_or_expense_btn_clicked)
        self._ui.add_expense_button.clicked.disconnect(self.add_income_or_expense_btn_clicked)

    def notify_view_loaded(self):
        """Emit main_view_loaded_signal to controller."""
        self.main_view_loaded_signal.emit(True)

    @pyqtSlot(dict)
    def display_transactions(self, data):
        """Display transactions in the view.

        Args:
            data (dict): the user's transactions
        """
        for item in data:
            self.transaction_data.add_transaction(item)

        # transactions displayed in tables, now update pie chart
        print(data)
        self.load_pie_chart_data(data)

    def load_pie_chart_data(self, data):
        """Load the pie chart with data.

        Args:
            income (list): list of income transactions
            expense (list): list of expense transactions
        """
        self._ui.pie_chart.update_data(data)

    def get_new_transaction_type(self):
        """Get the type of transaction to add.

        Returns:
            bool: True if income, False if expense
        """
        if self._ui.tab_bar.currentIndex() == 0:
            return True
        if self._ui.tab_bar.currentIndex() == 2:
            return False
    
    def add_income_or_expense_btn_clicked(self):
        """Handle add income button clicked signal."""
        # TODO: 
        # - implement tags
        # - refactor?
        
        if self._ui.tab_bar.currentIndex() == 2:
            amount = self._ui.expense_amount_line_edit.text()
            if amount == "":
                self.display_field_error()
                return
            new_expense = {
                "amount": amount,
                "date": self._ui.expense_date_edit.date().toString(Qt.DateFormat.ISODate),
                "description": self._ui.expense_description_text_edit.toPlainText(),
                "is_income": False,
            }
            self.add_income_btn_clicked_signal.emit(new_expense)
            self._ui.expense_amount_line_edit.clear()
            self._ui.expense_description_text_edit.clear()
        else: # can only be income tab
            amount = self._ui.income_amount_line_edit.text()
            if amount == "":
                self.display_field_error()
                return
            new_income = {
                "amount": amount,
                "date": self._ui.income_date_edit.date().toString(Qt.DateFormat.ISODate),
                "description": self._ui.income_description_text_edit.toPlainText(),
                "is_income": True,
            }
            self.add_income_btn_clicked_signal.emit(new_income)
            self._ui.income_amount_line_edit.clear()
            self._ui.income_description_text_edit.clear()

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