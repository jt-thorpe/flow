from PyQt6.QtWidgets import QMainWindow

from views.login_window_view import LoginWindowView
from views.main_tabs_ui import Ui_main_tabs_window


class MainAppView(QMainWindow):
    """MainApp view."""

    def __init__(self):
        """Initialize MainApp view."""
        super().__init__()

        self._ui = Ui_main_tabs_window()
        self._ui.setupUi(self)

        # Show login window
        self.login_window_view = LoginWindowView()
