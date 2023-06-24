import sys

from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class LoginController(QObject):
    """LoginWindow controller.

    Handles signals from the LoginWindow view and Model. Passes data from the
    view to the model and vice versa.

    Attributes:
        authentication_request_signal (pyqtSignal): sent to model
        controller_auth_res_signal (pyqtSignal): sent to view
    """

    authentication_request_signal = pyqtSignal(tuple)  # sent to model
    controller_auth_res_signal = pyqtSignal(bool)  # sent to view

    def __init__(self, model, view):
        """Initialize LoginWindow controller."""
        super().__init__()

        self._model = model  # the model object
        self._view = view  # the login view object

        # Connect view signals to controller slots
        self._view.login_req_signal.connect(self.handle_login_signal)  # login
        self._view.exit_req_signal.connect(self.handle_exit_signal)  # exit

        # connect controller signals to model slots
        self.authentication_request_signal.connect(
            self._model.authenticate_user)

        # connect model signals to controller slots
        self._model.model_auth_signal.connect(
            self.handle_authentication_signal)

        # connect controller signals to view slots
        self.controller_auth_res_signal.connect(
            self._view.handle_login_result_signal)

    @pyqtSlot(bool)
    def handle_login_signal(self):
        """Handle login request from view."""
        login_request_details = self._view.get_login_info()
        self.request_authentication(login_request_details)

    @pyqtSlot(bool)
    def handle_exit_signal(self):
        """Handle exit request from view.

        TODO:
            - easier to sys.exit() here or in the view?
            - probably the view... is middle man controller necessary for this?
        """
        sys.exit()

    def request_authentication(self, login_request_details):
        """Request authentication from model.

        Args:
            login_request_details (tuple): (email, password)
        """
        self.authentication_request_signal.emit(login_request_details)

    @pyqtSlot(bool)
    def handle_authentication_signal(self, login_result):
        """Handle login result from model.

        Args:
            login_result (bool): True if login successful, False otherwise
        """
        self.controller_auth_res_signal.emit(login_result)
