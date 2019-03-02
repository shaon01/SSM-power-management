import sys
from PyQt5 import QtWidgets
from GuiLayOut2 import Ui_MainWindow
from SerialConnect import SerialConnect


class AppWindow(QtWidgets.QMainWindow):
    serialCom = SerialConnect()
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_kl15.clicked.connect(self.btnKl15Clicked)
        self.ui.btn_SSM_A.clicked.connect(self.btnSSM_AClicked)
        self.ui.btn_SSM_B.clicked.connect(self.btnSSM_BClicked)
        self.ui.btn_Power.clicked.connect(self.btnPowerClicked)
        self.ui.btn_connect.clicked.connect(self.btnReconnectClicked)
        if self.serialCom.serialStatus is 'CONNECTED':
            initLable = 'ON'
            initColr = 'green'
        else:
            initLable = 'unknown'
            initColr = 'red'
        self.setALLlable(initColr, initLable)
        self.setComStatus()

    def btnKl15Clicked(self):
        colr, text = self.serialCom.get_kl_15_Status()
        self.ui.lbl_kl15.setStyleSheet('background-color:'+colr)
        self.ui.lbl_kl15.setText(text)

    def btnSSM_AClicked(self):
        colr, text = self.serialCom.get_kl_30_SSM_A_Status()
        self.ui.lbl_SSM_A.setText(text)
        self.ui.lbl_SSM_A.setStyleSheet('background-color:'+colr)

    def btnSSM_BClicked(self):
        colr, text = self.serialCom.get_kl_30_SSM_B_Status()
        self.ui.lbl_SSM_B.setText(text)
        self.ui.lbl_SSM_B.setStyleSheet('background-color:' + colr)

    def btnPowerClicked(self):
        colr, text = self.serialCom.getRebootStatus()
        self.setALLlable(colr, text)

    def btnReconnectClicked(self):
        colr, comStat = self.serialCom.reconnectSerial()
        if comStat is self.serialCom.comOn:
            text = 'ON'
        else:
            text = 'OFF'
        self.setALLlable(colr, text)
        self.setComStatus()

    def setALLlable(self,colr,text):
        self.ui.lbl_kl15.setText(text)
        self.ui.lbl_kl15.setStyleSheet('background-color:' + colr)
        self.ui.lbl_SSM_A.setText(text)
        self.ui.lbl_SSM_A.setStyleSheet('background-color:' + colr)
        self.ui.lbl_SSM_B.setText(text)
        self.ui.lbl_SSM_B.setStyleSheet('background-color:' + colr)
        self.ui.lbl_Power.setText(text)
        self.ui.lbl_Power.setStyleSheet('background-color:' + colr)

    def setComStatus(self):
        if self.serialCom.serialStatus is self.serialCom.comOn:
            self.ui.bar_ComStatus.setValue(100)
            self.ui.btn_connect.setText('CONNECTED')
        else:
            self.ui.bar_ComStatus.setValue(0)
            self.ui.btn_connect.setText('RECONNECT')



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = AppWindow()
    application.show()
    sys.exit(app.exec())