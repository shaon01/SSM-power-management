import  SerialConnect


def printOptions():
	print ("****************************")
	print ("Turn on kl 15 		=> k \nTurn off kl 15 		=> f")
	print ("Turn on kl 30 		=> p \nTurn off kl 30		=> s ")
	print ("Turn on all power	=> h \nTurn off all power	=> d")
	print ("Reboot the system	=> r")
	print ("To quit the program	=> q")
	print ("****************************\n")


printOptions()

sendSerial = SerialConnect.SerialConnect()


while True:
	#print "To see the option => a"
	userInput = input("Give the user action: ")
	if userInput is 'q':
		exit()
	sendSerial.sendData(userInput)
	
	







