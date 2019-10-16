
import platform
print(platform.node())
import sys
from QT_GUI.SerialConnect import SerialConnect

commandIndex = 1	
					 # Avaliabe for both tower and remainnig CI machines
serialCommandList = {'startkl15': 'k',
                     'stopkl15': 'f',
					 
					 # Used for tower
					 'startkl30A': 'q',
                     'stopkl30A': 'w',
                     'startkl30B': 'e',
                     'stopkl30B': 'r',
					 
					 # Used for remaining CI machines
					 'startkl30': 'p',
					 'stopkl30': 's',
					 
					 # Only avaliable for tower
                     'DTC_EF3011':'z',
                     'DTC_EF3012':'x',
                     'DTC_EF3013':'c',
                     'DTC_None':'v'}

def printHelp():
	print('===========================================')
	print('               HELP WINDOW                 ')
	print('===========================================')
	print('KL15 and KL30 commands')
	print('Start KL 15:  startkl15')
	print('Stop  KL 15:  stopkl15')
	print('')

	print('CI machines specific')
	print('Start KL 30:  startkl30')
	print('Stop  KL 30:  stopkl30')
	print('')

	print('Tower specific')
	print('Start KL 30 A-side:  startkl30A')
	print('Stop  KL 30 A-side:  stopkl30A')
	print('Start KL 30 B-side:  startkl30B')
	print('Stop  KL 30 B-side:  stopkl30B')
	print('')

	print('Q-diode DTC commands')
	print('Activate DTC EF3011: DTC_EF3011')
	print('Activate DTC EF3012: DTC_EF3012')
	print('Activate DTC EF3013: DTC_EF3013')
	print('Deactivate all DTCs: DTC_None')
	print('')

	print('Help command:  h')
	print('===========================================')

if len(sys.argv) > commandIndex:
	inputArg = str(sys.argv[commandIndex])
	if inputArg is 'h':
		printHelp()
	
	# If not tower then convert the side specific commands to the common
	if platform.node() not in 'SSM-TOWER-1':
		if 'startkl30' in inputArg:
			inputArg = 'startkl30'
		elif 'stopkl30' in inputArg:
			inputArg = 'stopkl30'

	if inputArg in serialCommandList:
		serialCLI = SerialConnect()

		val, status = serialCLI.comSerialStatus()
		if status is serialCLI.comOn:
            #print('Received option:', inputArg, ';; Serial value:', serialCommandList.get(inputArg))
			serialCLI.sendData(serialCommandList.get(inputArg))
		else:
			print('Power supply is not available')
	else:
		print('Option is not valid')
		printHelp()
else:
    print('No argument is given, please provide one of the following option')
    printHelp()
