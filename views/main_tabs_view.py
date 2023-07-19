from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from views.main_tabs_ui import Ui_main_tabs_window


class MainAppView(QMainWindow):
    """MainApp view."""

    main_view_loaded_signal = pyqtSignal(bool)

    def __init__(self):
        """Initialize MainApp view."""
        super().__init__()

        self._ui = Ui_main_tabs_window()
        self._ui.setupUi(self)

        self._ui.tab_bar.setCurrentIndex(1)  # set to dashboard tab

    def notify_view_loaded(self):
        """Emit main_view_loaded_signal to controller."""
        self.main_view_loaded_signal.emit(True)

    @pyqtSlot(dict)
    def display_transactions(self, data):
        """Display transactions in the view.

        Args:
            data (dict): the user's transactions
        """
        self._ui.income_table.setRowCount(len(data["income"]))
        self._ui.expense_table.setRowCount(len(data["expenses"]))

        i = 0
        for item in data["income"]:
            item_amount = QTableWidgetItem(str(item.amount))
            item_amount.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_date = QTableWidgetItem(str(item.date))
            item_date.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_description = QTableWidgetItem(item.description)
            self._ui.income_table.setItem(i, 0, item_amount)
            self._ui.income_table.setItem(i, 1, item_date)
            self._ui.income_table.setItem(i, 2, item_description)
            i += 1

        i = 0
        for item in data["expenses"]:
            item_amount = QTableWidgetItem(str(item.amount))
            item_amount.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_date = QTableWidgetItem(str(item.date))
            item_date.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_description = QTableWidgetItem(item.description)
            self._ui.expense_table.setItem(i, 0, item_amount)
            self._ui.expense_table.setItem(i, 1, item_date)
            self._ui.expense_table.setItem(i, 2, item_description)
            i += 1
