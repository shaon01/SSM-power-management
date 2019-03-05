from tkinter import *
from time import sleep
import serial
import sys

import serial.tools.list_ports

        

class SerialConnect:

	srlCom = serial.Serial()
	srlCom.baudrate = 9600
	kl15Status = "UNKNOWN"
	kl30Status = "UNKNOWN"
	io_arduino_on =  0
	io_arduino_off = 1
	io_status_on =  'ON'
	io_status_off = 'OFF'
	rbtStatus  = "UNKNOWN"

	#arduino serial command
	kl15on 	= 	'k'
	kl15off = 	'f'
	kl30_on 	= 'p'
	kl30_off = 's'
	pwron	= 	'h'
	pwroff	=	'd'
	io_status = 'i'

	io_kl15_id = 'f'
	io_kl30_id = 't'

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
			self.getArduinoIOstatus()
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

	#reading current arduino value from serial
	def getArduinoIOstatus(self):
		if self.serialStatus is self.comOn:
			self.sendData(self.io_status)
			while self.srlCom.inWaiting() > 0:
				rawVal = self.srlCom.readline()
			serialData = list(rawVal.decode('utf-8'))
			# looking for kl15 status
			if self.io_kl15_id in serialData:
				indexOf15id = serialData.index(self.io_kl15_id) + 1
				if int(serialData[indexOf15id]) is self.io_arduino_off:
					self.kl15Status = self.io_status_off
				elif int(serialData[indexOf15id]) is self.io_arduino_on:
					self.kl15Status = self.io_status_on

			# looking for kl30 status
			if self.io_kl30_id in serialData:
				indexOf30id = serialData.index(self.io_kl30_id) + 1
				if int(serialData[indexOf30id]) is self.io_arduino_off:
					self.kl30Status = self.io_status_off
				elif int(serialData[indexOf30id]) is self.io_arduino_on:
					self.kl30Status = self.io_status_on
		print('kl 15 status : ', self.kl15Status, 'arduino status :', serialData[indexOf15id])
		print('kl 30 status : ', self.kl30Status, 'arduino status :', serialData[indexOf30id])
		print('========================================')


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
		if self.serialStatus is self.comOn:
			self.getArduinoIOstatus()
			if self.kl15Status is self.io_status_on:
				colr="red"
				serVal = self.kl15off
			elif self.kl15Status is self.io_status_off:
				colr="green"
				serVal = self.kl15on
			self.sendData(serVal)
			self.getArduinoIOstatus()
		return colr, self.kl15Status
	
# send kl 30 ssm_a serial to contorl and set the button value
	def get_kl_30_SSM_A_Status(self):
		colr="red"
		if self.serialStatus is self.comOn:
			self.getArduinoIOstatus()
			if self.kl30Status is self.io_status_on:
				colr="red"
				serVal = self.kl30_off
			elif self.kl30Status is self.io_status_off:
				colr="green"
				serVal = self.kl30_on
			self.sendData(serVal)
			self.getArduinoIOstatus()
		return colr, self.kl30Status

	# send all power contol
	def getRebootStatus(self):
		colr="red"
		if self.serialStatus is self.comOn:
			if self.rbtStatus is self.io_status_on:
				self.rbtStatus = self.io_status_off
				colr = "red"
				serVal = self.pwroff 
			elif self.rbtStatus is self.io_status_off:
				self.rbtStatus = self.io_status_on
				colr = "green"
				serVal = self.pwron
			self.sendData(serVal)
			self.getArduinoIOstatus()
		return colr, self.rbtStatus
	
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



