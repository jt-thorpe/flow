import sys

from PyQt6.QtWidgets import QApplication

import flow_app_resources  # nb: doesn't need accessing, just importing
from views.login_window_view import LoginWindowView


class FlowApp(QApplication):
    def __init__(self, sys_argv):
        super(FlowApp, self).__init__(sys_argv)

        self.login_window_view = LoginWindowView()
        self.login_window_view.show()


if __name__ == '__main__':
    app = FlowApp(sys.argv)
    sys.exit(app.exec())
