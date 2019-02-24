from tkinter import *
from time import sleep
import serial
import sys

import serial.tools.list_ports

        

class SerialConnect:
	
	kl15Status = "unknown"
	kl30Status = "unknown"
	rbtStatus  = "unknown" 

	kl15on 	= 	'k'
	kl15off = 	'f'
	kl30on 	= 	'p'
	kl30off = 	's'
	pwron	= 	'h'
	pwroff	=	'd'
	reboot 	=	'r'
	serialStatus = 'DISCONNECTED'
	
	def __init__(self):
		try:
			self.srlCom = serial.Serial(self.getComProt(), 9600)
			self.serialStatus = 'CONNECTED'
			self.kl15Status = "ON"
			self.kl30Status = "ON"
			self.rbtStatus  = "ON"
		except (OSError, serial.SerialException):
			self.serialStatus = 'DISCONNECTED'
			pass
		
	def sendData(self,powerCmd):
		try:
			self.srlCom.write(str.encode(powerCmd)) 
			sleep(.1) # Delay for one tenth of a second
		except (OSError, serial.SerialException):
			self.serialStatus = 'DISCONNECTED'
			pass
		
# send kl 15 serial to contorl and set the button value
	def get_kl_15_Status(self):
		colr="red"
		if self.serialStatus is 'CONNECTED':
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
		colr="red"
		if self.serialStatus is 'CONNECTED':
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
		colr="red"
		if self.serialStatus is 'CONNECTED':
			if self.rbtStatus is "ON":
				self.rbtStatus = "OFF"
				colr = "red"
				serVal = self.pwroff 
			elif self.rbtStatus is "OFF":
				self.rbtStatus = "ON"
				colr = "green"
				serVal = self.pwron
			self.sendData(serVal)
		return colr,self.rbtStatus	
	
# get all the ports and get the necessry port
	def getComProt(self):
		arduinoPortID = ''
		ports = serial.tools.list_ports.comports()
		if sys.platform.startswith('win'):
			for port in ports :
				if str(port.manufacturer).startswith('Arduino'):
					#print 'found it in windows:',port.device
					arduinoPortID = port.device
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			for port in ports :
				if str(port.manufacturer).startswith('Arduino'):
					#print 'found it:',port.device
					arduinoPortID = port.device
		return arduinoPortID
        
			
		
			
    

test = SerialConnect()
print(test.serialStatus)

