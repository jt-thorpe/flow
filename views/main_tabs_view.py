from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow

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
