# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(400, 473)
        self.verticalLayout = QtWidgets.QVBoxLayout(login_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_frame = QtWidgets.QFrame(parent=login_window)
        self.logo_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.logo_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.infinity_logo = QtWidgets.QLabel(parent=self.logo_frame)
        self.infinity_logo.setText("")
        self.infinity_logo.setPixmap(QtGui.QPixmap("img/infinity_256x256.png"))
        self.infinity_logo.setObjectName("infinity_logo")
        self.horizontalLayout_4.addWidget(
            self.infinity_logo, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.logo_frame)
        self.email_frame = QtWidgets.QFrame(parent=login_window)
        self.email_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.email_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.email_frame.setObjectName("email_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.email_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.email_icon = QtWidgets.QLabel(parent=self.email_frame)
        self.email_icon.setText("")
        self.email_icon.setPixmap(QtGui.QPixmap("img/mail_32x32.png"))
        self.email_icon.setObjectName("email_icon")
        self.horizontalLayout_3.addWidget(self.email_icon)
        self.email_input = QtWidgets.QLineEdit(parent=self.email_frame)
        self.email_input.setObjectName("email_input")
        self.horizontalLayout_3.addWidget(self.email_input)
        self.hide_email_btn = QtWidgets.QPushButton(parent=self.email_frame)
        self.hide_email_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/hidden_32x32.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.hide_email_btn.setIcon(icon)
        self.hide_email_btn.setIconSize(QtCore.QSize(24, 24))
        self.hide_email_btn.setCheckable(True)
        self.hide_email_btn.setObjectName("hide_email_btn")
        self.horizontalLayout_3.addWidget(self.hide_email_btn)
        self.verticalLayout.addWidget(self.email_frame)
        self.password_frame = QtWidgets.QFrame(parent=login_window)
        self.password_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.password_frame.setObjectName("password_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.password_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lock_icon = QtWidgets.QLabel(parent=self.password_frame)
        self.lock_icon.setText("")
        self.lock_icon.setPixmap(QtGui.QPixmap("img/lock_32x32.png"))
        self.lock_icon.setObjectName("lock_icon")
        self.horizontalLayout_2.addWidget(self.lock_icon)
        self.password_input = QtWidgets.QLineEdit(parent=self.password_frame)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.horizontalLayout_2.addWidget(self.password_input)
        self.hide_password_btn = QtWidgets.QPushButton(
            parent=self.password_frame)
        self.hide_password_btn.setText("")
        self.hide_password_btn.setIcon(icon)
        self.hide_password_btn.setIconSize(QtCore.QSize(24, 24))
        self.hide_password_btn.setCheckable(True)
        self.hide_password_btn.setObjectName("hide_password_btn")
        self.horizontalLayout_2.addWidget(self.hide_password_btn)
        self.verticalLayout.addWidget(self.password_frame)
        self.button_frame = QtWidgets.QFrame(parent=login_window)
        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(parent=self.button_frame)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        self.exit_btn = QtWidgets.QPushButton(parent=self.button_frame)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        self.verticalLayout.addWidget(self.button_frame)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Form"))
        self.email_input.setPlaceholderText(
            _translate("login_window", "Enter your email"))
        self.password_input.setPlaceholderText(
            _translate("login_window", "Enter your password"))
        self.login_btn.setText(_translate("login_window", "Login"))
        self.exit_btn.setText(_translate("login_window", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QWidget()
    ui = Ui_LoginWindow()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec())