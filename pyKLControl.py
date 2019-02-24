from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port


def printOptions():
	print "****************************"
	print "Turn on kl 15 		=> k \nTurn off kl 15 		=> f"
	print "Turn on kl 30 		=> p \nTurn off kl 30		=> s "
	print "Turn on all power	=> h \nTurn off all power	=> d" 
	print "Reboot the system	=> r"
	print "To quit the program	=> q"
	print "****************************\n"


def sendPowerCmd(pwrCmd):
	ser.write(str(pwrCmd)) 
	print ser.readline() 
	sleep(.1) # Delay for one tenth of a second








printOptions()


while True:
	#print "To see the option => a"
	userInput = raw_input("Give the user action: ")
	if userInput is 'q':
		exit()
	sendPowerCmd(userInput)
	
	







