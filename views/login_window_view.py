from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow

from views.login_window_ui import Ui_login_main_window


class LoginWindowView(QMainWindow):
    """LoginWindow view."""

    # View signals
    login_req_signal = pyqtSignal(bool)
    exit_req_signal = pyqtSignal(bool)

    def __init__(self):
        """Initialize LoginWindow view."""
        super().__init__()

        self._ui = Ui_login_main_window()
        self._ui.setupUi(self)

        # Connect signals to slots
        self._ui.login_button.clicked.connect(self.__login_button_event)
        self._ui.exit_button.clicked.connect(self.__exit_button_event)

    def __login_button_event(self):
        """Emit login_req_signal to controller."""
        self.login_req_signal.emit(True)

    def __exit_button_event(self):
        """Emit exit_req_signal to controller."""
        self.exit_req_signal.emit(True)

    def get_login_info(self):
        """Return login info from view."""
        return (self._ui.email_input.text(), self._ui.password_input.text())

    def clear_login_info(self):
        """Clear login info from view."""
        self._ui.email_input.clear()
        self._ui.password_input.clear()
