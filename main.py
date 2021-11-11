import processHandler
import os
from tkinter import *
from tkinter import ttk
import psutil

# create list for processes
labels = []
#GUI window
root = Tk()

def setup():

    # Setup title and size of GUI
    root.title("Linux Task Manager")
    root.geometry("1000x400")
    root.resizable(True, True)

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
    frame_Net = LabelFrame(tab_proc, text = "Network", width=150)
    frame_Disk = LabelFrame(tab_proc, text = "Disk", width=150)
    frame_Mem = LabelFrame(tab_proc, text = "Memory", width=150)
    frame_CPU = LabelFrame(tab_proc, text = "CPU", width=150)
    frame_ProcName = LabelFrame(tab_proc, text = "Process Name")
    # Put names into GUI tab
    frame_Net.pack(fill = "y", side = "right")
    frame_Disk.pack(fill = "y", side = "right")
    frame_Mem.pack(fill = "y", side = "right")
    frame_CPU.pack(fill = "y", side = "right")
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
    button_quit = Button(frame_ProcName, text="Quit", command = lambda:root.destroy()).grid(row=1, column=0)
    
    listProcesses(2, frame_ProcName)
    procList()

    root.mainloop()
    

# Get list of active processes
def procList():

    # Array to hold process info
    procArr = []

    # Iterate through processes and get PID, name, and username
    for proc in psutil.process_iter(['pid', 'name', 'username']):

        # temp hold variables for process info
        pid = proc.pid
        name = proc.name()
        user = proc.username()

        # Add process to the list of processes
        procArr.append((pid, name, user)) 
    # # Return list of processes
    return procArr     


# Print list of active processes in GUI
# posStart = the next free row position in frameName
# frameName = the frame that the processes will be listed in
def listProcesses(posStart, frameName):

    # temp variable for row position
    r = posStart

    # Iterate through processes and get PID, name, and username
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        # temp column variable
        c=0
        # temp hold variables for process info
        pid = proc.pid
        name = proc.name()
        user = proc.username()
        # Put Process info into the frame
        Label(frameName, text=pid).grid(row=r, column=c)
        c+=1
        Label(frameName, text=name).grid(row=r, column=c)
        c+=1
        Label(frameName, text=user).grid(row=r, column=c)
        r+=1


# delete and recreate process list
def update():
    global labels
    for x in labels:
        (pID, name) = x
        pID.set("")
        name.set("")
    labels.clear()

# def updateProcList(pos, frame):
#     while True:
#         listProcesses(pos, frame)
#         self.after(1000,updateProcList(pos, frame))
#     # create()

# callback function for button. Kills process
def killCallBack(pID):
    processHandler.killProcess(pID)
    update()


def main():

    setup()

    # # inital process list
    # create()


    root.mainloop()


if __name__ == '__main__':
    main()
