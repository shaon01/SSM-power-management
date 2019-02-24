from tkinter import *

from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
 
window = Tk()
 
window.title("Power Manager")
 
window.geometry('640x480')


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

 
lbl_KL_15 = Label(window, bg="green", text="ON",height=2, width=5)
lbl_KL_15.grid(column=2, row=1)

lbl_KL_30 = Label(window,bg="green", text="ON",height=2, width=5)
lbl_KL_30.grid(column=2, row=2)

lbl_reboot = Label(window,bg="green", text="ON",height=2, width=5)
lbl_reboot.grid(column=2, row=3, padx=5,pady=5)

def sendPowerCmd(pwrCmd):
	ser.write(str(pwrCmd)) 
	sleep(.1) # Delay for one tenth of a second

 
def clickedKL15():
	global kl15Status
	if kl15Status is "ON":
		kl15Status= "OFF"
		colr="red"
		serVal = kl15off
	elif kl15Status is "OFF":
		kl15Status = "ON"
		colr="green"
		serVal = kl15on
	sendPowerCmd(serVal)
	lbl_KL_15.configure(bg=colr,text=kl15Status)
	
	
    
def clickedKL30():
	global kl30Status
	if kl30Status is "ON":
		kl30Status= "OFF"
		colr="red"
		serVal = kl30off
	elif kl30Status is "OFF":
		kl30Status = "ON"
		colr="green"
		serVal = kl30on
	sendPowerCmd(serVal)
	lbl_KL_30.configure(bg=colr,text=kl30Status)
    
def clickedReboot():
	global rbtStatus
	if rbtStatus is "ON":
		rbtStatus= "OFF"
		colr="red"
		serVal = pwroff
	elif rbtStatus is "OFF":
		rbtStatus = "ON"
		colr="green"
		serVal = pwron
	sendPowerCmd(serVal)
	lbl_reboot.configure(bg=colr,text=rbtStatus)
	lbl_KL_30.configure(bg=colr,text=rbtStatus)
	lbl_KL_15.configure(bg=colr,text=rbtStatus)


btn_KL_15 = Button(window, text="KL 15 Toggle", command=clickedKL15)
btn_KL_15.grid(column=1, row=1,padx=50,pady=25)

btn_KL_30 = Button(window, text="KL 30 Toggle", command=clickedKL30)
btn_KL_30.grid(column=1, row=2,padx=50,pady=25)

btn_reboot = Button(window, text="All power", command=clickedReboot)
btn_reboot.grid(column=1, row=3,padx=50,pady=25)
 

window.mainloop()
