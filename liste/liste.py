# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 40, 160, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_edit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_edit.setObjectName("btn_edit")
        self.verticalLayout.addWidget(self.btn_edit)
        self.btn_reomve = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_reomve.setObjectName("btn_reomve")
        self.verticalLayout.addWidget(self.btn_reomve)
        self.btn_up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_up.setObjectName("btn_up")
        self.verticalLayout.addWidget(self.btn_up)
        self.btn_down = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_down.setObjectName("btn_down")
        self.verticalLayout.addWidget(self.btn_down)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "add"))
        self.btn_edit.setText(_translate("MainWindow", "edit"))
        self.btn_reomve.setText(_translate("MainWindow", "remove"))
        self.btn_up.setText(_translate("MainWindow", "up"))
        self.btn_down.setText(_translate("MainWindow", "down"))
        self.pushButton_7.setText(_translate("MainWindow", "sort"))
        self.btn_exit.setText(_translate("MainWindow", "exit"))
