from tkinter import *
import  SerialConnect
import sys

class PowerSupplyGUI:
	
	serialClass = SerialConnect.SerialConnect()
	
	def __init__(self,window):
		if self.serialClass.serialStatus is 'CONNECTED':
			initLable = 'ON'
			initColr = 'green'
		else:
			initLable = 'unknown'
			initColr = 'red'  
		# lable for kl15
		self.lbl_KL_15 = Label(window, bg=initColr, text=initLable,height=2, width=7)
		self.lbl_KL_15.grid(column=2, row=1)
		# lable for kl30
		self.lbl_KL_SSM_A = Label(window,bg=initColr, text=initLable,height=2, width=7)
		self.lbl_KL_SSM_A.grid(column=2, row=2)
		# lable for all power
		self.lbl_power = Label(window,bg=initColr, text=initLable,height=2, width=7)
		self.lbl_power.grid(column=2, row=3, padx=5,pady=5)
		# label for connection status
		self.lbl_comStat = Label(window,bg=initColr, text=self.serialClass.serialStatus,height=2, width=15)
		self.lbl_comStat.grid(column=2, row=4, padx=5,pady=5)

		# label for connection status
		self.lbl_comTitle = Label(window,text='Com Status',height=2, width=15)
		self.lbl_comTitle.grid(column=1, row=4, padx=5,pady=5)
		
		self.btn_KL_15 = Button(window, text="KL 15 Toggle", command=self.clickedKL15)
		self.btn_KL_15.grid(column=1, row=1,padx=50,pady=25)

		self.btn_KL_30 = Button(window, text="KL 30 Toggle", command=self.clickedKL30)
		self.btn_KL_30.grid(column=1, row=2,padx=50,pady=25)

		self.btn_reboot = Button(window, text="All power", command=self.clickedReboot)
		self.btn_reboot.grid(column=1, row=3,padx=50,pady=25)

		self.btn_connect = Button(window, text="reconnect", command=self.clickedConnect)
		self.btn_connect.grid(column=3, row=4,padx=50,pady=25)
		self.updateLable()
		
		
	def updateLable(self):
		if self.serialClass.comSerialStatus() is self.serialClass.comOff:
			#print (self.serialClass.comSerialStatus())
			colr = 'red'
			status = 'unknown'
			comStat = 'DISCONNECTED'
			self.lbl_KL_15.configure(bg=colr,text=status)
			self.lbl_KL_SSM_A.configure(bg=colr,text=status)
			self.lbl_power.configure(bg=colr,text=status)
			self.lbl_comStat.configure(bg=colr,text=comStat)
			#calling update in 1000 milisecond
		#self.lbl_KL_15.after(10, self.updateLable)
		#self.lbl_KL_SSM_A.after(10, self.updateLable)
		#self.lbl_power.after(10, self.updateLable)
		self.lbl_comStat.after(1000, self.updateLable)
			
			
	# lable handeler for kl15
	def clickedKL15(self):
		colr,kl15Status = self.serialClass.get_kl_15_Status()
		self.lbl_KL_15.configure(bg=colr,text=kl15Status)
		
	# lable handeler for kl30
	def clickedKL30(self):
		colr,kl30Status = self.serialClass.get_kl_30_Status()
		self.lbl_KL_SSM_A.configure(bg=colr,text=kl30Status)

	# lable handeler for power for all
	def clickedReboot(self):
		colr,rbtStatus = self.serialClass.getRebootStatus()
		self.lbl_power.configure(bg=colr,text=rbtStatus)
		self.lbl_KL_SSM_A.configure(bg=colr,text=rbtStatus)
		self.lbl_KL_15.configure(bg=colr,text=rbtStatus)
		
	def clickedConnect(self):
		colr,comState = self.serialClass.reconnectSerial()
		self.lbl_comStat.configure(bg=colr,text=comState)




if __name__ == '__main__':
	window = Tk()
	PowerSupplyGUI(window)
	window.title("Power Manager")
	window.geometry('640x480')
	window.mainloop()

