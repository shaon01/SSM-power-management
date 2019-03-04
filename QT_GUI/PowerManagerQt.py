import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from GuiLayOut2 import Ui_MainWindow
from SerialConnect import SerialConnect


class AppWindow(QtWidgets.QMainWindow):
    serialCom = SerialConnect()
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #setting button handler for each button
        self.ui.btn_kl15.clicked.connect(self.btnKl15Clicked)
        self.ui.btn_SSM_A.clicked.connect(self.btnSSM_AClicked)
        self.ui.btn_SSM_B.clicked.connect(self.btnSSM_BClicked)
        self.ui.btn_Power.clicked.connect(self.btnPowerClicked)
        self.ui.btn_connect.clicked.connect(self.btnReconnectClicked)
        self.happyDog = QtGui.QPixmap('happyDog.jpg')
        self.sadDog = QtGui.QPixmap('sadDog.jpg')
        self.setInitialStatus()



    def setInitialStatus(self):
        if self.serialCom.serialStatus is self.serialCom.comOn:
            initLable = 'ON'
            initColr = 'green'
        else:
            initLable = 'UNKNOWN'
            initColr = 'red'
        self.setALLlable(initColr, initLable)
        self.setComStatus()

    # kl15 button handeler
    def btnKl15Clicked(self):
        colr, text = self.serialCom.get_kl_15_Status()
        self.ui.lbl_kl15.setStyleSheet('background-color:'+colr)
        self.ui.lbl_kl15.setText(text)

    # ssm_A kl30 button handeler
    def btnSSM_AClicked(self):
        colr, text = self.serialCom.get_kl_30_SSM_A_Status()
        self.ui.lbl_SSM_A.setText(text)
        self.ui.lbl_SSM_A.setStyleSheet('background-color:'+colr)

    # ssm_B kl30 button handeler
    def btnSSM_BClicked(self):
        colr, text = self.serialCom.get_kl_30_SSM_B_Status()
        self.ui.lbl_SSM_B.setText(text)
        self.ui.lbl_SSM_B.setStyleSheet('background-color:' + colr)

    # all power button handeler
    def btnPowerClicked(self):
        colr, text = self.serialCom.getRebootStatus()
        self.setALLlable(colr, text)

    # reconnect button handeler
    def btnReconnectClicked(self):
        colr, comStat = self.serialCom.reconnectSerial()
        if comStat is self.serialCom.comOn:
            text = 'ON'
        else:
            text = 'OFF'
        self.setALLlable(colr, text)
        self.setComStatus()

    #update all the labels at the same time
    def setALLlable(self,colr,text):
        self.ui.lbl_kl15.setText(text)
        self.ui.lbl_kl15.setStyleSheet('background-color:' + colr)
        self.ui.lbl_SSM_A.setText(text)
        self.ui.lbl_SSM_A.setStyleSheet('background-color:' + colr)
        self.ui.lbl_SSM_B.setText(text)
        self.ui.lbl_SSM_B.setStyleSheet('background-color:' + colr)
        self.ui.lbl_Power.setText(text)
        self.ui.lbl_Power.setStyleSheet('background-color:' + colr)

    #Set status of com button and the status bar
    def setComStatus(self):
        if self.serialCom.serialStatus is self.serialCom.comOn:
            self.ui.bar_ComStatus.setValue(100)
            self.ui.btn_connect.setText('CONNECTED')
            self.ui.lbl_miri.setPixmap(self.happyDog)
        else:
            self.ui.bar_ComStatus.setValue(0)
            self.ui.btn_connect.setText('RECONNECT')
            self.ui.lbl_miri.setPixmap(self.sadDog)

    #recheck the serial connection status in run time
    def updateComStatus(self):
        colr, comStat = self.serialCom.comSerialStatus()
        if comStat is self.serialCom.comOff:
            text = 'UNKNOWN'
            self.setALLlable(colr, text)
            self.setComStatus()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = AppWindow()
    timer = QtCore.QTimer()
    timer.timeout.connect(application.updateComStatus)
    timer.start(1000)  # every 10,000 milliseconds
    application.show()
    sys.exit(app.exec())