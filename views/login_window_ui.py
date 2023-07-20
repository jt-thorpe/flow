# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login_main_window(object):
    def setupUi(self, login_main_window):
        login_main_window.setObjectName("login_main_window")
        login_main_window.resize(401, 469)
        self.central_widget = QtWidgets.QWidget(parent=login_main_window)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.logo_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.logo_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.infinity_logo = QtWidgets.QLabel(parent=self.logo_frame)
        self.infinity_logo.setText("")
        self.infinity_logo.setPixmap(QtGui.QPixmap(
            ":/resources/img/infinity_256x256.png"))
        self.infinity_logo.setObjectName("infinity_logo")
        self.horizontalLayout_4.addWidget(
            self.infinity_logo, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.logo_frame)
        self.login_fail_message = QtWidgets.QLabel(parent=self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.login_fail_message.setFont(font)
        self.login_fail_message.setStyleSheet("QLabel {color: red;}")
        self.login_fail_message.setObjectName("login_fail_message")
        self.login_fail_message.hide()
        self.verticalLayout.addWidget(
            self.login_fail_message, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.email_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.email_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.email_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.email_frame.setObjectName("email_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.email_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.email_icon = QtWidgets.QLabel(parent=self.email_frame)
        self.email_icon.setText("")
        self.email_icon.setPixmap(QtGui.QPixmap(
            ":/resources/img/mail_32x32.png"))
        self.email_icon.setObjectName("email_icon")
        self.horizontalLayout_3.addWidget(self.email_icon)
        self.email_input = QtWidgets.QLineEdit(parent=self.email_frame)
        self.email_input.setObjectName("email_input")
        self.horizontalLayout_3.addWidget(self.email_input)
        self.hide_email_button = QtWidgets.QPushButton(parent=self.email_frame)
        self.hide_email_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/img/hidden_32x32.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.hide_email_button.setIcon(icon)
        self.hide_email_button.setIconSize(QtCore.QSize(24, 24))
        self.hide_email_button.setCheckable(True)
        self.hide_email_button.setObjectName("hide_email_button")
        self.horizontalLayout_3.addWidget(self.hide_email_button)
        self.verticalLayout.addWidget(self.email_frame)
        self.password_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.password_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.password_frame.setObjectName("password_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.password_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lock_icon = QtWidgets.QLabel(parent=self.password_frame)
        self.lock_icon.setText("")
        self.lock_icon.setPixmap(QtGui.QPixmap(
            ":/resources/img/lock_32x32.png"))
        self.lock_icon.setObjectName("lock_icon")
        self.horizontalLayout_2.addWidget(self.lock_icon)
        self.password_input = QtWidgets.QLineEdit(parent=self.password_frame)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.horizontalLayout_2.addWidget(self.password_input)
        self.hide_password_button = QtWidgets.QPushButton(
            parent=self.password_frame)
        self.hide_password_button.setText("")
        self.hide_password_button.setIcon(icon)
        self.hide_password_button.setIconSize(QtCore.QSize(24, 24))
        self.hide_password_button.setCheckable(True)
        self.hide_password_button.setObjectName("hide_password_button")
        self.horizontalLayout_2.addWidget(self.hide_password_button)
        self.verticalLayout.addWidget(self.password_frame)
        self.button_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_button = QtWidgets.QPushButton(parent=self.button_frame)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.exit_button = QtWidgets.QPushButton(parent=self.button_frame)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.verticalLayout.addWidget(self.button_frame)
        login_main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(login_main_window)
        QtCore.QMetaObject.connectSlotsByName(login_main_window)

    def retranslateUi(self, login_main_window):
        _translate = QtCore.QCoreApplication.translate
        login_main_window.setWindowTitle(
            _translate("login_main_window", "Flow"))
        self.login_fail_message.setText(_translate(
            "login_main_window", "Login unsucessful: please try again"))
        self.email_input.setPlaceholderText(
            _translate("login_main_window", "Enter your email"))
        self.password_input.setPlaceholderText(
            _translate("login_main_window", "Enter your password"))
        self.login_button.setText(_translate("login_main_window", "Login"))
        self.exit_button.setText(_translate("login_main_window", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_main_window = QtWidgets.QMainWindow()
    ui = Ui_login_main_window()
    ui.setupUi(login_main_window)
    login_main_window.show()
    sys.exit(app.exec())
