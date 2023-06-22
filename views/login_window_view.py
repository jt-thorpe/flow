from PyQt6.QtWidgets import QMainWindow

from views.login_window_ui import Ui_login_main_window


class LoginWindowView(QMainWindow):
    """LoginWindow view."""
    def __init__(self):
        """Initialize LoginWindow view."""
        super().__init__()

        self._ui = Ui_login_main_window()
        self._ui.setupUi(self)
