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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
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
        self.income_table.setGeometry(QtCore.QRect(15, 20, 371, 800))
        self.income_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.income_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.income_table.setObjectName("income_table")
        self.income_table.setColumnCount(3)
        self.income_table.setRowCount(0)
        self.income_table.horizontalHeader().setStretchLastSection(True)
        item = QtWidgets.QTableWidgetItem()
        self.income_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.income_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.income_table.setHorizontalHeaderItem(2, item)
        self.add_income_btn = QtWidgets.QPushButton(parent=self.income_tab)
        self.add_income_btn.setGeometry(QtCore.QRect(640, 240, 141, 41))
        self.add_income_btn.setObjectName("add_income_btn")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.income_tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(410, 20, 371, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.add_income_form_layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.add_income_form_layout.setContentsMargins(0, 0, 0, 0)
        self.add_income_form_layout.setObjectName("add_income_form_layout")
        self.income_amount_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.income_amount_label.setObjectName("income_amount_label")
        self.add_income_form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.income_amount_label)
        self.income_amount_line_edit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.income_amount_line_edit.setObjectName("income_amount_line_edit")
        self.add_income_form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.income_amount_line_edit)
        self.income_date_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.income_date_label.setObjectName("income_date_label")
        self.add_income_form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.income_date_label)
        self.income_date_edit = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        self.income_date_edit.setObjectName("income_date_edit")
        self.add_income_form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.income_date_edit)
        self.income_tags_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.income_tags_label.setObjectName("income_tags_label")
        self.add_income_form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.income_tags_label)
        self.income_description_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.income_description_label.setObjectName("income_description_label")
        self.add_income_form_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.income_description_label)
        self.income_description_text_edit = QtWidgets.QPlainTextEdit(parent=self.formLayoutWidget)
        self.income_description_text_edit.setObjectName("income_description_text_edit")
        self.add_income_form_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.income_description_text_edit)
        self.income_tags_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.income_tags_combo_box.setObjectName("income_tags_combo_box")
        self.add_income_form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.income_tags_combo_box)
        self.tab_bar.addTab(self.income_tab, "")
        self.dashboard_tab = QtWidgets.QWidget()
        self.dashboard_tab.setObjectName("dashboard_tab")
        self.tab_bar.addTab(self.dashboard_tab, "")
        self.expense_tab = QtWidgets.QWidget()
        self.expense_tab.setObjectName("expense_tab")
        self.expense_table = QtWidgets.QTableWidget(parent=self.expense_tab)
        self.expense_table.setGeometry(QtCore.QRect(804, 20, 371, 800))
        self.expense_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.expense_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.expense_table.setObjectName("expense_table")
        self.expense_table.setColumnCount(3)
        self.expense_table.setRowCount(0)
        self.expense_table.horizontalHeader().setStretchLastSection(True)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(2, item)
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.expense_tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(410, 20, 371, 211))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.add_expense_form_layout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.add_expense_form_layout.setContentsMargins(0, 0, 0, 0)
        self.add_expense_form_layout.setObjectName("add_expense_form_layout")
        self.expense_amount_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.expense_amount_label.setObjectName("expense_amount_label")
        self.add_expense_form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.expense_amount_label)
        self.expense_amount_line_edit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.expense_amount_line_edit.setObjectName("expense_amount_line_edit")
        self.add_expense_form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_amount_line_edit)
        self.expense_date_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.expense_date_label.setObjectName("expense_date_label")
        self.add_expense_form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.expense_date_label)
        self.expense_date_edit = QtWidgets.QDateEdit(parent=self.formLayoutWidget_2)
        self.expense_date_edit.setObjectName("expense_date_edit")
        self.add_expense_form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_date_edit)
        self.expense_tag_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.expense_tag_label.setObjectName("expense_tag_label")
        self.add_expense_form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.expense_tag_label)
        self.expense_description_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.expense_description_label.setObjectName("expense_description_label")
        self.add_expense_form_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.expense_description_label)
        self.expense_description_text_edit = QtWidgets.QPlainTextEdit(parent=self.formLayoutWidget_2)
        self.expense_description_text_edit.setObjectName("expense_description_text_edit")
        self.add_expense_form_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_description_text_edit)
        self.expense_tag_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.expense_tag_combo_box.setObjectName("expense_tag_combo_box")
        self.add_expense_form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.expense_tag_combo_box)
        self.add_expense_button = QtWidgets.QPushButton(parent=self.expense_tab)
        self.add_expense_button.setGeometry(QtCore.QRect(410, 240, 141, 41))
        self.add_expense_button.setObjectName("add_expense_button")
        self.tab_bar.addTab(self.expense_tab, "")
        self.verticalLayout.addWidget(self.tab_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_bar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.income_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.income_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.income_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        self.add_income_btn.setText(_translate("MainWindow", "Add Income"))
        self.income_amount_label.setText(_translate("MainWindow", "Amount"))
        self.income_date_label.setText(_translate("MainWindow", "Date"))
        self.income_tags_label.setText(_translate("MainWindow", "Tags"))
        self.income_description_label.setText(_translate("MainWindow", "Description"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(self.income_tab), _translate("MainWindow", "Income"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(self.dashboard_tab), _translate("MainWindow", "Dashboard"))
        item = self.expense_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.expense_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.expense_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        self.expense_amount_label.setText(_translate("MainWindow", "Amount"))
        self.expense_date_label.setText(_translate("MainWindow", "Date"))
        self.expense_tag_label.setText(_translate("MainWindow", "Tags"))
        self.expense_description_label.setText(_translate("MainWindow", "Description"))
        self.add_expense_button.setText(_translate("MainWindow", "Add Expense"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(self.expense_tab), _translate("MainWindow", "Expense"))
