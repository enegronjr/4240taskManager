# 4240 Clemson Fall 2021
# Linux Task Manager
# Breanna Filipiak, Eddie Negron, Sterling Rich

from typing import FrozenSet
import processHandler
import os
from tkinter import *
from tkinter import ttk
import psutil

#GUI window
root = Tk()

# Sets up the GUI window for the application
def setup():

    # Setup title and size of GUI
    root.title("Linux Task Manager")
    root.geometry("500x500")
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
    
    # Functions to create the Label Frames tat hold the process information
    makeProcNameFrame(tab_proc)
    makePerformanceFrame(tab_perf)
    makeUsersFrame(tab_user)

    # Tkinter function to continue to run the GUI
    root.mainloop()

# Creates the frame with the process names
# tabName = The parent of the frame
def makeProcNameFrame(tabName):
    
    """ PROCESS TAB SETUP """

    #Create the frame
    frame_proc = ttk.Frame(tabName)
    frame_proc.pack(fill="both", expand="yes")
    
    # Create subframes
    frame_topBar = LabelFrame(frame_proc, height=30)
    frame_Mem = LabelFrame(frame_proc, text = "Memory", width=250)
    frame_CPU = LabelFrame(frame_proc, text = "CPU", width=250)
    frame_ProcName = LabelFrame(frame_proc, text = "Process Name")

    # Put names into GUI tab
    frame_topBar.pack(fill='x', side='top')
    frame_Mem.pack(fill = "y", side = "right")
    frame_CPU.pack(fill = "y", side = "right")
    frame_ProcName.pack(fill = "both", expand="yes", side = "right")

    # String variable that holds PID
    pid_var = StringVar()
    # Label for the PID "to kill"
    label_ProcID = Label(frame_topBar, text="pID").grid(row=0, column=1)
    # Entry for the PID "to kill"
    entry_ProcID = Entry(frame_topBar, textvariable=pid_var).grid(row=0, column=2)
    # Button for the PID "to kill"
    button_killProc = Button(frame_topBar, text="Kill", command = lambda:killCallBack(pid_var.get())).grid(row=0, column=3)
    # Button to quit the app
    button_quit = Button(frame_topBar, text="Quit", command = lambda:root.destroy()).grid(row=1, column=0)
    # Button to "refresh" the current list of running processes
    button_listProcs = Button(frame_topBar, text="List Processes", command = lambda:refreshProcFrame(tabName, frame_proc)).grid(row=0, column=0)
    # List actively running processes
    listProcesses(3, frame_ProcName, frame_CPU, frame_Mem)
    

# Refreshes the list of actively running processes
# tabName = the parent frame of 'frameName'
# frameName = the frame being "refreshed"
def refreshProcFrame(tabName, frameName):
    # Destroy frameName
    frameName.destroy()
    # Remake frameName within tabName
    makeProcNameFrame(tabName)

# Creates the frame with process performance information
# tabName = name of the parent frame
def makePerformanceFrame(tabName):
    
    # create the frame
    frame_Performance = LabelFrame(tabName, text="Performance")
    frame_Performance.pack(fill = "both", expand = "yes")

    # button to refresh preformance stats
    button_refresh = Button(frame_Performance, text="Refresh", command=lambda:refreshPrefFrame(tabName, frame_Performance)).grid(row=0, column=0)
    # button to quit the app
    button_quit = Button(frame_Performance, text="Quit", command = lambda:root.destroy()).grid(row=0, column=1)
    # Label for cpu usage
    label_cpu = Label(frame_Performance, text="CPU", font=('Arial',16)).grid(row=1, column=0)
    label_cpuUsage = Label(frame_Performance, text=(str(psutil.cpu_percent()) + '%')).grid(row=1, column=2)
    # Label for memory usage
    mem = psutil.virtual_memory()
    gb = 1000000000
    label_mem = Label(frame_Performance, text="Memory", font=('Arial',16)).grid(row=2, column=0)
    label_memUsage = Label(frame_Performance, text=(str(round((mem.total - mem.available)/gb, 1)) + '/' + str(round(mem.total/gb, 1)) + ' GB  ' + str(mem.percent) + '%')).grid(row=2, column=2)
    # Label for disk usage
    disk = psutil.disk_usage('/')
    label_disk = Label(frame_Performance, text="Disk", font=('Arial',16)).grid(row=3, column=0)
    label_diskUsage = Label(frame_Performance, text=(str(disk.percent) + '%')).grid(row=3, column=2)

# Refresh the frame with the performance information
# tabName = parent of the frame being refreshed
# frameName = name of the frame that is being refreshed
def refreshPrefFrame(tabName, frameName):
    frameName.destroy()
    makePerformanceFrame(tabName)

# Creates the frame that holds user process information
# tabName = name of the parent frame
def makeUsersFrame(tabName):
    # Create the frame
    frame_Users = LabelFrame(tabName, text="Users")
    frame_Users.pack(fill ="both", expand="yes")

    # Button to refresh users
    button_refresh = Button(frame_Users, text="Refresh", command=lambda:refreshUsersFrame(tabName, frame_Users)).grid(row=0, column=0)
    # Button to quit the app
    button_quit = Button(frame_Users, text="Quit", command = lambda:root.destroy()).grid(row=0, column=1)

    # Create Labels with usernames for each process
    r = 1
    for user in psutil.users():
        Label(frame_Users, text=str(user.name)).grid(row=r, column=0)
        r+=1

# Refreshes the frame with the user process information
# tabName = the parent frame of the frame that is being refreshed
# frameName = the name of the frame that is being refreshed
def refreshUsersFrame(tabName, frameName):
    frameName.destroy()
    makeUsersFrame(tabName)   


# Print list of active processes in GUI
# posStart = the next free row position in frameName
# frameName = the frame that the processes will be listed in
def listProcesses(posStart, frameName, frameCpu, frameMem):

    # temp variable for row position
    r = posStart

    procs = []
    # Iterate through processes and get PID, name, and username
    for proc in psutil.process_iter():
        # temp hold variables for process info
        pid = proc.pid
        name = proc.name()
        user = proc.username()
        mem = round(proc.memory_percent(), 2)
        cpu = proc.cpu_percent()
        procs.append((pid, name, user, mem, cpu))

    procs.sort(reverse=True)

    for proc in procs:
        # temp column variable
        c=0
        # Put Process info into the frame
        Label(frameName, text=proc[0]).grid(row=r, column=c)
        c+=1
        Label(frameName, text=proc[1]).grid(row=r, column=c)
        c+=1
        Label(frameName, text=proc[2]).grid(row=r, column=c)
        Label(frameCpu, text=proc[4], width=15).grid(row=r, column=0)
        Label(frameMem, text=proc[3], width=15).grid(row=r, column=0)
        r+=1

# delete and recreate process list
def update():
    global labels
    for x in labels:
        (pID, name) = x
        pID.set("")
        name.set("")
    labels.clear()

# callback function for button. Kills process
def killCallBack(pID):
    processHandler.killProcess(pID)
    update()

def main():
    setup()
    root.mainloop()

if __name__ == '__main__':
    main()
