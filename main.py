import processHandler
import os
from tkinter import *



# create list for processes
labels = []
root = Tk()

# create process list
def create():
    global labels, root

    # get list of processes
    procArr = processHandler.getProcesses()
    
    i = 0
    for x in procArr:
        (pID, name) = x 
        pIDLabel_var = StringVar(root, str(pID))
        nameLabel_var = StringVar(root, name)

        Label(root, text=str(pID), textvariable=pIDLabel_var).grid(column=0, row=i)
        Label(root, text=name, textvariable=nameLabel_var).grid(column=1, row=i)
        labels.append((pIDLabel_var, nameLabel_var))
        i = i + 1

# delete and recreate process list
def update():
    global labels
    for x in labels:
        (pID, name) = x
        pID.set("")
        name.set("")
    labels.clear()
    create()

# callback function for button. Kills process
def killCallBack(pID):
    processHandler.killProcess(pID)
    update()


def main():
    # create textbox 
    pid_var = StringVar()
    Label(root, text="pID").grid(column=4, row=0)
    Entry(root, textvariable = pid_var).grid(column=5, row=0)

    # inital process list
    create()

    Button(root, text="Kill", command = lambda:killCallBack(pid_var.get())).grid(column=5, row=1)
    Button(root, text="Quit", command = lambda:root.destroy()).grid(column=6, row=1)
    root.mainloop()


if __name__ == '__main__':
    main()