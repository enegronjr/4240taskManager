import processHandler
import os
from tkinter import *
from tkinter import ttk

#GUI window
root = Tk()


# Setup title and size of GUI
root.title("Linux Task Manager")
root.geometry("1000x400")

""" TAB MANAGEMENT """

# Create tab manager
tabs = ttk.Notebook(root)
# Create tabs
tab_proc = ttk.Frame(root)
tab_perf = ttk.Frame(root)
tab_user = ttk.Frame(root)
# Add tabs to tab manager
tabs.add(tab_proc, text="Processes")
tabs.add(tab_perf, text="Performance")
tabs.add(tab_user, text="Users")
# Put tab manager in GUI
tabs.pack(expand=1, fill='both')

""" PROCESS TAB SETUP """

# Create Frames
frame_Net = LabelFrame(tab_proc, text = "Network", width=100)
frame_Disk = LabelFrame(tab_proc, text = "Disk", width=100)
frame_Mem = LabelFrame(tab_proc, text = "Memory", width=100)
frame_CPU = LabelFrame(tab_proc, text = "CPU", width=100)
frame_ProcName = LabelFrame(tab_proc, text = "Process Name")
frame_ProcList = LabelFrame(tab_proc, width=200)
# Put names into GUI tab
frame_Net.pack(fill = "y", side = "right")
frame_Disk.pack(fill = "y", side = "right")
frame_Mem.pack(fill = "y", side = "right")
frame_CPU.pack(fill = "y", side = "right")
frame_ProcList.pack(fill = "x", side = "bottom")
frame_ProcName.pack(fill = "both", expand = "yes", side = "right")

""" PROCESS NAMES """

# String variable that holds PID
pid_var = StringVar()
# Label for the PID "to kill"
label_ProcID = Label(frame_ProcName, text="pID").grid(row=0, column=0)
# Entry for the PID "to kill"
entry_ProcID = Entry(frame_ProcName, textvariable=pid_var).grid(row=0, column=1)
# Button for the PID "to kill"
button_killProc = Button(frame_ProcName, text="Kill", command = lambda:killCallBack(pid_var.get())).grid(row=0, column=2)
# Button to quit the app
button_quit = Button(frame_ProcName, text="Quit", command = lambda:root.destroy()).grid(row=3, column=0)

scrollbarProcesses = Scrollbar(frame_ProcList)
scrollbarProcesses.pack(side = "right", fill = "y")

labels = Listbox(frame_ProcList, yscrollcommand=scrollbarProcesses.set)

# create process list
def create():
    global labels, root

    # get list of processes
    procArr = processHandler.getProcesses()
    
    for x in procArr:
        (pID, name) = x 
        labels.insert(END, name + "    " + str(pID))

    labels.pack(side = 'left', fill = "both")

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

    # setup()

    # # inital process list
    create()


    root.mainloop()


if __name__ == '__main__':
    main()
