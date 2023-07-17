# Form implementation generated from reading ui file 'main_tabs.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_main_tabs_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(800, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_bar = QtWidgets.QTabWidget(parent=self.frame)
        self.tab_bar.setMinimumSize(QtCore.QSize(800, 600))
        self.tab_bar.setStyleSheet("QTabBar::tab { height: 50px; width: 125px;}\n"
                                   "QTabWidget::tab-bar {alignment: center;}")
        self.tab_bar.setObjectName("tab_bar")
        self.income_tab = QtWidgets.QWidget()
        self.income_tab.setObjectName("income_tab")
        self.income_table = QtWidgets.QTableWidget(parent=self.income_tab)
        self.income_table.setGeometry(QtCore.QRect(15, 20, 330, 800))
        self.income_table.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.income_table.setObjectName("income_table")
        self.income_table.setColumnCount(3)
        self.income_table.setRowCount(0)
        self.income_table.setHorizontalHeaderLabels(
            ["Amount", "Date", "Description"])
        self.income_input = QtWidgets.QLineEdit(parent=self.income_tab)
        self.income_input.setGeometry(QtCore.QRect(390, 80, 113, 25))
        self.income_input.setObjectName("income_input")
        self.add_income_btn = QtWidgets.QPushButton(parent=self.income_tab)
        self.add_income_btn.setGeometry(QtCore.QRect(390, 250, 80, 25))
        self.add_income_btn.setObjectName("add_income_btn")
        self.income_desc = QtWidgets.QTextEdit(parent=self.income_tab)
        self.income_desc.setGeometry(QtCore.QRect(390, 120, 271, 111))
        self.income_desc.setObjectName("income_desc")
        self.tab_bar.addTab(self.income_tab, "")
        self.dashboard_tab = QtWidgets.QWidget()
        self.dashboard_tab.setObjectName("dashboard_tab")
        self.tab_bar.addTab(self.dashboard_tab, "")
        self.expense_tab = QtWidgets.QWidget()
        self.expense_tab.setObjectName("expense_tab")
        self.expense_table = QtWidgets.QTableWidget(parent=self.expense_tab)
        self.expense_table.setGeometry(QtCore.QRect(845, 20, 330, 800))
        self.expense_table.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.expense_table.setObjectName("expense_table")
        self.expense_table.setColumnCount(3)
        self.expense_table.setRowCount(0)
        self.expense_table.setHorizontalHeaderLabels(
            ["Amount", "Date", "Description"])
        self.expense_input = QtWidgets.QLineEdit(parent=self.expense_tab)
        self.expense_input.setGeometry(QtCore.QRect(440, 20, 113, 25))
        self.expense_input.setObjectName("expense_input")
        self.add_expense_btn = QtWidgets.QPushButton(parent=self.expense_tab)
        self.add_expense_btn.setGeometry(QtCore.QRect(470, 190, 80, 25))
        self.add_expense_btn.setObjectName("add_expense_btn")
        self.expense_desc = QtWidgets.QTextEdit(parent=self.expense_tab)
        self.expense_desc.setGeometry(QtCore.QRect(280, 60, 271, 111))
        self.expense_desc.setObjectName("expense_desc")
        self.tab_bar.addTab(self.expense_tab, "")
        self.verticalLayout.addWidget(self.tab_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_bar.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.income_input.setPlaceholderText(
            _translate("MainWindow", "Enter income"))
        self.add_income_btn.setText(_translate("MainWindow", "Add Income"))
        self.income_desc.setPlaceholderText(_translate(
            "MainWindow", "Add an optional description of the income"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(
            self.income_tab), _translate("MainWindow", "Income"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(
            self.dashboard_tab), _translate("MainWindow", "Dashboard"))
        self.expense_input.setPlaceholderText(
            _translate("MainWindow", "Enter expense"))
        self.add_expense_btn.setText(_translate("MainWindow", "Add Expense"))
        self.expense_desc.setPlaceholderText(_translate(
            "MainWindow", "Add an optional description of the expense"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(
            self.expense_tab), _translate("MainWindow", "Expense"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
