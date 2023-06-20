from PyQt6 import QMainWindow
from PyQt6.QtCore import pyqtSlot

from views.login_window_ui import Ui_LoginWindow


class LoginWindowView(QMainWindow):
    """LoginWindow view.

    Responsible for connecting signals from ui widgets to controller methods
    and updating ui widgets based on model changes.

    Attributes:
        _model: LoginWindow model.
        _login_controller: LoginWindow controller.
        _ui: LoginWindow ui.
    """

    def __init__(self, model, login_controller):
        """Initialize LoginWindow view."""
        super().__init__()

        self._model = model
        self._login_controller = login_controller
        self._ui = Ui_LoginWindow()
        self._ui.setupUi(self)

        # Some code to connect signals etc goes here + methods for updating ui

    @pyqtSlot(str)
    def on_update_email(self, email):
        """Update email input."""
        self._ui.email_input.setText(email)

    @pyqtSlot(str)
    def on_update_password(self, password):
        """Update password input."""
        self._ui.password_input.setText(password)
