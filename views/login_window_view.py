import sys
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow

from views.login_window_ui import Ui_login_main_window


class LoginWindowView(QMainWindow):
    """LoginWindow view.

    TODO: hook up hide/show password and email buttons
    """

    # View signals
    login_req_signal = pyqtSignal(bool)  # sent to controller
    exit_req_signal = pyqtSignal(bool)  # sent to controller

    def __init__(self):
        """Initialize LoginWindow view."""
        super().__init__()

        self._ui = Ui_login_main_window()
        self._ui.setupUi(self)

    def set_up_connections(self):
        """Set up login_view connections."""
        self._ui.login_button.clicked.connect(
            self._send_login_req_signal)
        self._ui.exit_button.clicked.connect(
            self.exit_requested)
        
    def clean_up_connections(self):
        """Clean up login_view connections."""
        self._ui.login_button.clicked.disconnect(
            self._send_login_req_signal)
        self._ui.exit_button.clicked.disconnect(
            self.exit_requested)

    def _send_login_req_signal(self):
        """Emit login_req_signal to controller."""
        self.login_req_signal.emit(True)

    def exit_requested(self):
        """Request exit from app."""
        self.exit_req_signal.emit(True)
        

    def get_login_info(self):
        """Return text from email and password inputs.

        Returns:
            tuple: (email, password)
        """
        return (self._ui.email_input.text(), self._ui.password_input.text())

    def clear_login_info(self):
        """Clear login info from view."""
        self._ui.email_input.clear()
        self._ui.password_input.clear()

    @pyqtSlot(bool)
    def handle_login_result_signal(self, login_result):
        """Handle login result from controller.

        Args:
            login_result (bool): True if login successful, False otherwise

        TODO:
            - do something with login_result, like show a message box
        """
        if login_result:
            self._ui.login_fail_message.hide()
            print('Login successful')
        else:
            self._ui.login_fail_message.show()
            self.clear_login_info()
            print('Login failed')
