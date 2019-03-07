import sys
from QT_GUI.SerialConnect import SerialConnect

commandIndex = 1
serialCommandList = {'startkl15': 'k',
                     'stopkl15': 'f',
                     'startkl30': 'p',
                     'stopkl30': 's'}

def printHelp():
    print('======================================')
    print('Command for Start    KL 15:  startkl15')
    print('Command for Stop     KL 15:  stopkl15')
    print('Command for Start    KL 30:  startkl30')
    print('Command for Stop     KL 30:  stopkl30')
    print('Command for help          :  h')
    print('======================================')

if len(sys.argv) > commandIndex:
    inputArg = str(sys.argv[commandIndex])
    if inputArg is 'h':
        printHelp()
    if inputArg in serialCommandList:
        serialCLI = SerialConnect()
        val, status = serialCLI.comSerialStatus()
        if status is serialCLI.comOn:
            print('Received option:', inputArg, ';; Serial value:', serialCommandList.get(inputArg))
            serialCLI.sendData(serialCommandList.get(inputArg))
        else:
            print('Power supply is not available')
    else:
        print('Option is not valid')
        printHelp()
else:
    print('No argument is given, please provide one of the following option')
    printHelp()
