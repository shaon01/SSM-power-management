from tkinter import *
from time import sleep
import serial
import sys

import serial.tools.list_ports

        

class SerialConnect:

	srlCom = serial.Serial()
	srlCom.baudrate = 9600
	kl15Status = "unknown"
	kl30Status = "unknown"
	rbtStatus  = "unknown" 

	kl15on 	= 	'k'
	kl15off = 	'f'
	kl30SSM_A_on 	= 'p'
	kl30SSM_A_off = 's'
	kl30SSM_B_on = 'p'
	kl30SSM_B_off = 's'
	pwron	= 	'h'
	pwroff	=	'd'
	reboot 	=	'r'
	comOn = 'CONNECTED'
	comOff = 'DISCONNECTED'
	serialStatus = comOn
	
	def __init__(self):
		try:
			self.srlCom.port = self.getComProt()
			self.srlCom.open()
			self.serialStatus = self.comOn
			self.kl15Status = "ON"
			self.kl30Status = "ON"
			self.rbtStatus  = "ON"
		except (OSError, serial.SerialException):
			self.serialStatus = self.comOff
			pass
			
	def reconnectSerial(self):
		try:
			self.srlCom.port = self.getComProt()
			self.srlCom.open()
			self.kl15Status = "ON"
			self.kl30Status = "ON"
			self.rbtStatus = "ON"
		except (OSError, serial.SerialException):
			pass
		colr, comStat = self.comSerialStatus()
		return colr, comStat
		
	def sendData(self,powerCmd):
		try:
			self.srlCom.write(str.encode(powerCmd)) 
			sleep(.1) # Delay for one tenth of a second
		except (OSError, serial.SerialException):
			self.serialStatus = self.comOff
			pass
			
	def comSerialStatus(self):
		if str(self.getComProt()) is '':
			colr = 'red'
			self.serialStatus = self.comOff
		else:
			colr ='green'
			self.serialStatus = self.comOn
		return colr, self.serialStatus
		
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
	
# send kl 30 ssm_a serial to contorl and set the button value
	def get_kl_30_SSM_A_Status(self):
		colr="red"
		if self.serialStatus is 'CONNECTED':
			if self.kl30Status is "ON":
				self.kl30Status= "OFF"
				colr="red"
				serVal = self.kl30SSM_A_off
			elif self.kl30Status is "OFF":
				self.kl30Status = "ON"
				colr="green"
				serVal = self.kl30SSM_A_on
			self.sendData(serVal)
		return colr,self.kl30Status

# send kl 30 ssm_a serial to contorl and set the button value
	def get_kl_30_SSM_B_Status(self):
		colr = "red"
		if self.serialStatus is 'CONNECTED':
			if self.kl30Status is "ON":
				self.kl30Status = "OFF"
				colr = "red"
				serVal = self.kl30SSM_B_off
			elif self.kl30Status is "OFF":
				self.kl30Status = "ON"
				colr = "green"
				serVal = self.kl30SSM_B_on
			#todo : need to implement serial values
			self.sendData(serVal)
		return colr, self.kl30Status

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



