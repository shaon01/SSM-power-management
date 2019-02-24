from tkinter import *
from time import sleep
import serial


class SerialConnect:
	
	kl15Status = "ON"
	kl30Status = "ON"
	rbtStatus  = "ON" 

	kl15on 	= 	'k'
	kl15off = 	'f'
	kl30on 	= 	'p'
	kl30off = 	's'
	pwron	= 	'h'
	pwroff	=	'd'
	reboot 	=	'r'
	
	
	def __init__(self):
		self.srlCom = serial.Serial('/dev/ttyACM0', 9600)
		
		
	def sendData(self,powerCmd):
		self.srlCom.write(str(powerCmd)) 
		sleep(.1) # Delay for one tenth of a second
		
# send kl 15 serial to contorl and set the button value
	def get_kl_15_Status(self):
		if self.kl15Status is "ON":
			self.kl15Status= "OFF"
			colr="red"
			serVal = self.kl15off
		elif self.kl15Status is "OFF":
			self.kl15Status = "ON"
			colr="green"
			serVal = self.kl15on
		self.sendData(serVal)
		return colr,self.kl15Status
	
# send kl 30 serial to contorl and set the button value		
	def get_kl_30_Status(self):
		if self.kl30Status is "ON":
			self.kl30Status= "OFF"
			colr="red"
			serVal = self.kl30off
		elif self.kl30Status is "OFF":
			self.kl30Status = "ON"
			colr="green"
			serVal = self.kl30on
		self.sendData(serVal)
		return colr,self.kl30Status

# send all power contol 
	def getRebootStatus(self):
		if self.rbtStatus is "ON":
			self.rbtStatus = "OFF"
			colr = "red"
			serVal = self.kl30off 
		elif self.rbtStatus is "OFF":
			self.rbtStatus = "ON"
			colr = "green"
			serVal = self.kl30on
		self.sendData(serVal)
		return colr,self.rbtStatus	
	

