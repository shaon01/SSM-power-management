import sys
from QT_GUI.SerialConnect import SerialConnect

commandIndex = 1
serialCommandList = {'startkl15': 'k',
                     'stopkl15': 'f',
                     'startkl30': 'p',
                     'stopkl30': 's'}

serialCLI = SerialConnect()
if len(sys.argv) > commandIndex:
    inputArg = str(sys.argv[commandIndex])
    if inputArg in serialCommandList:
        print('In python received argument:', inputArg)
        print('serial command for received:', serialCommandList.get(inputArg))
        serialCLI.sendData(serialCommandList.get(inputArg))

else:
    print('no argument is given')
