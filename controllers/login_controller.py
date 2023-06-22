import sys

from PyQt6.QtCore import QObject, pyqtSlot

from models.flow_app_model import FlowModel
from views.login_window_view import LoginWindowView


class LoginController(QObject):
    """LoginWindow controller.

    Handles signals from the LoginWindow view and Model. Passes data from the
    view to the model and vice versa.
    """

    def __init__(self, model, view):
        """Initialize LoginWindow controller."""
        super().__init__()

        self._model = model  # the model object
        self._view = view  # the login view object

        # Connect view signals to controller slots
        self._view.login_req_signal.connect(self.login_request)  # login
        self._view.exit_req_signal.connect(self.exit_app)  # exit

    @pyqtSlot(bool)
    def login_request(self):
        """Handle login request from view."""
        print('Login request received by controller.')
        login_info = self._view.get_login_info()
        print(f'Login info: {login_info}')
        self._view.clear_login_info()

    @pyqtSlot(bool)
    def exit_app(self):
        """Exit the application."""
        sys.exit()
