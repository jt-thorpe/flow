import sys

from PyQt6.QtCore import pyqtSlot, QEvent
from PyQt6.QtWidgets import QApplication

import flow_app_resources  # nb: doesn't need accessing, just importing
from controllers.login_controller import LoginController
from controllers.main_view_controller import MainViewController
from models.flow_app_model import FlowModel
from views.login_window_view import LoginWindowView
from views.main_tabs_view import MainAppView


class FlowApp(QApplication):
    def __init__(self, sys_argv):
        super(FlowApp, self).__init__(sys_argv)

        # Initialize the model, views, and controller
        self.flow_app_model = FlowModel()
        self.login_window_view = LoginWindowView()
        self.login_controller = LoginController(self.flow_app_model,
                                                self.login_window_view)
        self.main_view_controller = None

        # setup external connections
        self.login_window_view.set_up_connections()
        self.login_controller.set_up_connections()

        # setup internal connections
        self.login_controller.proceed_to_main_signal.connect(
            self.switch_to_main_window)
        self.login_window_view.exit_req_signal.connect(self.exit_login)

        # show login window
        self.login_window_view.show()

    @pyqtSlot(bool)
    def switch_to_main_window(self):
        """Cleanup login window and switch to main window."""
        self.login_window_view.clean_up_connections()
        self.login_controller.clean_up_connections()
        self.login_window_view.close()

        if not hasattr(self, "main_app_view"):
            self.main_app_view = MainAppView()
            self.main_view_controller = MainViewController(self.flow_app_model,
                                                           self.main_app_view)
            self.main_app_view.set_up_connections()
            self.main_view_controller.set_up_connections()
            self.main_app_view.notify_view_loaded()
            self.main_app_view.show()        

    @pyqtSlot()
    def exit_login(self):
        """Cleanup login window and exit."""
        self.login_window_view.clean_up_connections()
        self.login_controller.clean_up_connections()  
        self.login_window_view.close()
        self.quit()


if __name__ == '__main__':
    app = FlowApp(sys.argv)
    app.exec()
