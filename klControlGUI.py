from tkinter import *
import  SerialConnect


serialClass = SerialConnect.SerialConnect() 
window = Tk()
 
window.title("Power Manager")
 
window.geometry('640x480')


# lable for kl15
lbl_KL_15 = Label(window, bg="green", text="ON",height=2, width=5)
lbl_KL_15.grid(column=2, row=1)
# lable for kl30
lbl_KL_30 = Label(window,bg="green", text="ON",height=2, width=5)
lbl_KL_30.grid(column=2, row=2)
# lable for all power
lbl_reboot = Label(window,bg="green", text="ON",height=2, width=5)
lbl_reboot.grid(column=2, row=3, padx=5,pady=5)

# lable handeler for kl15
def clickedKL15():
	colr,kl15Status = serialClass.get_kl_15_Status()
	lbl_KL_15.configure(bg=colr,text=kl15Status)
	
# lable handeler for kl30
def clickedKL30():
	colr,kl30Status = serialClass.get_kl_30_Status()
	lbl_KL_30.configure(bg=colr,text=kl30Status)

# lable handeler for power for all
def clickedReboot():
	colr,rbtStatus = serialClass.getRebootStatus()
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
