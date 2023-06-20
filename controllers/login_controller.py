from PyQt6.QtCore import QObject, pyqtSlot


class LoginController(QObject):
    """LoginWindow controller.

    Handles signals from ui widgets and updates model, and authenticates user.
    """

    def __init__(self, model):
        """Initialize LoginWindow controller."""
        super().__init__()
        self._model = model

    @pyqtSlot(str)
    def update_email(self, email):
        """Update email input."""
        self._model.email = email

    @pyqtSlot(str)
    def update_password(self, password):
        """Update password input."""
        self._model.password = password

    def authenticate(self):
        """Authenticate user."""
        self._model.authenticate()
