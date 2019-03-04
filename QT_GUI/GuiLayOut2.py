# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiLayOut2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ControlGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.ControlGroup.setGeometry(QtCore.QRect(30, 20, 331, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ControlGroup.setFont(font)
        self.ControlGroup.setObjectName("ControlGroup")
        self.btn_Power = QtWidgets.QPushButton(self.ControlGroup)
        self.btn_Power.setGeometry(QtCore.QRect(10, 150, 141, 31))
        self.btn_Power.setAutoFillBackground(False)
        self.btn_Power.setDefault(True)
        self.btn_Power.setFlat(False)
        self.btn_Power.setObjectName("btn_Power")
        self.lbl_SSM_A = QtWidgets.QLabel(self.ControlGroup)
        self.lbl_SSM_A.setGeometry(QtCore.QRect(190, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_SSM_A.setFont(font)
        self.lbl_SSM_A.setAutoFillBackground(False)
        self.lbl_SSM_A.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.lbl_SSM_A.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbl_SSM_A.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_SSM_A.setObjectName("lbl_SSM_A")
        self.lbl_kl15 = QtWidgets.QLabel(self.ControlGroup)
        self.lbl_kl15.setGeometry(QtCore.QRect(190, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_kl15.setFont(font)
        self.lbl_kl15.setAutoFillBackground(False)
        self.lbl_kl15.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.lbl_kl15.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbl_kl15.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_kl15.setObjectName("lbl_kl15")
        self.btn_kl15 = QtWidgets.QPushButton(self.ControlGroup)
        self.btn_kl15.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.btn_kl15.setAutoFillBackground(False)
        self.btn_kl15.setDefault(True)
        self.btn_kl15.setFlat(False)
        self.btn_kl15.setObjectName("btn_kl15")
        self.btn_SSM_A = QtWidgets.QPushButton(self.ControlGroup)
        self.btn_SSM_A.setGeometry(QtCore.QRect(10, 70, 141, 31))
        self.btn_SSM_A.setAutoFillBackground(False)
        self.btn_SSM_A.setDefault(True)
        self.btn_SSM_A.setFlat(False)
        self.btn_SSM_A.setObjectName("btn_SSM_A")
        self.btn_SSM_B = QtWidgets.QPushButton(self.ControlGroup)
        self.btn_SSM_B.setGeometry(QtCore.QRect(10, 110, 141, 31))
        self.btn_SSM_B.setAutoFillBackground(False)
        self.btn_SSM_B.setDefault(True)
        self.btn_SSM_B.setFlat(False)
        self.btn_SSM_B.setObjectName("btn_SSM_B")
        self.lbl_SSM_B = QtWidgets.QLabel(self.ControlGroup)
        self.lbl_SSM_B.setGeometry(QtCore.QRect(190, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_SSM_B.setFont(font)
        self.lbl_SSM_B.setAutoFillBackground(False)
        self.lbl_SSM_B.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.lbl_SSM_B.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbl_SSM_B.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_SSM_B.setObjectName("lbl_SSM_B")
        self.lbl_Power = QtWidgets.QLabel(self.ControlGroup)
        self.lbl_Power.setGeometry(QtCore.QRect(190, 150, 121, 31))
        self.lbl_Power.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Power.setFont(font)
        self.lbl_Power.setAutoFillBackground(False)
        self.lbl_Power.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.lbl_Power.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbl_Power.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Power.setObjectName("lbl_Power")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 280, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_connect = QtWidgets.QPushButton(self.groupBox)
        self.btn_connect.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.btn_connect.setAutoFillBackground(False)
        self.btn_connect.setDefault(True)
        self.btn_connect.setFlat(False)
        self.btn_connect.setObjectName("btn_connect")
        self.bar_ComStatus = QtWidgets.QProgressBar(self.groupBox)
        self.bar_ComStatus.setGeometry(QtCore.QRect(160, 30, 191, 31))
        self.bar_ComStatus.setProperty("value", 0)
        self.bar_ComStatus.setObjectName("bar_ComStatus")
        self.lbl_miri = QtWidgets.QLabel(self.centralwidget)
        self.lbl_miri.setGeometry(QtCore.QRect(400, 30, 200, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_miri.sizePolicy().hasHeightForWidth())
        self.lbl_miri.setSizePolicy(sizePolicy)
        self.lbl_miri.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_miri.setText("")
        self.lbl_miri.setScaledContents(True)
        self.lbl_miri.setObjectName("lbl_miri")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Power Manager"))
        self.ControlGroup.setTitle(_translate("MainWindow", "Control"))
        self.btn_Power.setText(_translate("MainWindow", "All Power"))
        self.lbl_SSM_A.setText(_translate("MainWindow", "OFF"))
        self.lbl_kl15.setText(_translate("MainWindow", "OFF"))
        self.btn_kl15.setText(_translate("MainWindow", "KL 15"))
        self.btn_SSM_A.setText(_translate("MainWindow", "SSM_A KL30"))
        self.btn_SSM_B.setText(_translate("MainWindow", "SSM_B KL30"))
        self.lbl_SSM_B.setText(_translate("MainWindow", "OFF"))
        self.lbl_Power.setText(_translate("MainWindow", "OFF"))
        self.groupBox.setTitle(_translate("MainWindow", "Connection Status"))
        self.btn_connect.setText(_translate("MainWindow", "Reconnect"))

