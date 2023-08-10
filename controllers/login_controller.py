from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class LoginController(QObject):
    """LoginWindow controller.

    Handles signals from the LoginWindow view and Model. Passes data from the
    view to the model and vice versa.

    Attributes:
        authentication_request_signal (pyqtSignal): sent to model
        controller_auth_res_signal (pyqtSignal): sent to view
        proceed_to_main_signal (pyqtSignal): sent to app

    Functions:
        handle_login_signal: handle login request from view
        handle_authentication_signal: handle login result from model
    """

    authentication_request_signal = pyqtSignal(tuple)
    controller_auth_res_signal = pyqtSignal(bool)
    proceed_to_main_signal = pyqtSignal(bool)

    def __init__(self, model, view):
        """Initialize LoginWindow controller."""
        super().__init__()

        self._model = model
        self._view = view

    def set_up_connections(self):
        """Set up login_controller connections."""
        self._view.login_req_signal.connect(
            self._handle_login_signal)
        self.authentication_request_signal.connect(
            self._model.authenticate_user)
        self.controller_auth_res_signal.connect(
            self._view.handle_login_result_signal)
        self._model.model_auth_signal.connect(
            self._handle_authentication_signal)

    def clean_up_connections(self):
        """Clean up login_controller connections."""
        self._view.login_req_signal.disconnect(
            self._handle_login_signal)
        self.authentication_request_signal.disconnect(
            self._model.authenticate_user)
        self.controller_auth_res_signal.disconnect(
            self._view.handle_login_result_signal)
        self._model.model_auth_signal.disconnect(
            self._handle_authentication_signal)

    @pyqtSlot(bool)
    def _handle_login_signal(self):
        """Handle login request from view."""
        login_request_details = self._view.get_login_info()
        self.authentication_request_signal.emit(login_request_details)

    @pyqtSlot(bool)
    def _handle_authentication_signal(self, login_result):
        """Handle login result from model.

        Args:
            login_result (bool): True if login successful, False otherwise
        """
        self.controller_auth_res_signal.emit(login_result)
        if login_result:
            self.proceed_to_main_signal.emit(True)
