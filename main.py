import processHandler
import os
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# get list of processes
procArr = processHandler.getProcesses()

# create list of processes
i = 0
for x in procArr:
    (pID, name) = x 
    ttk.Label(frm, text=str(pID)).grid(column=0, row=i)
    ttk.Label(frm, text=name).grid(column=1, row=i)
    i = i + 1


# create textbox 
pid_var = StringVar()
ttk.Label(frm, text="pID").grid(column=4, row=0)
ttk.Entry(frm, textvariable = pid_var).grid(column=5, row=0)


# callback function for button. Kills process
def killCallBack():
    command = "kill -9 "
    os.system(command + pid_var.get())
    print("killed" + pid_var.get())


killButton = ttk.Button(frm, text="Kill", command = killCallBack).grid(column=5, row=1)
root.mainloop()