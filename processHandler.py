import subprocess
import os

# processes are listed in /proc

def getProcesses():
    os.system("ls -lt /proc | grep '^d' > processes")
    f = open('processes')


    procArr = []
    for x in f:
        pID = str(x[65:-1])
        if pID.isnumeric():
            try:
                return_val = subprocess.check_output(["cat", "/proc/" + pID + "/comm"])
            except:
                print("error")
            else:
                return_val = str(return_val)
                return_val = return_val[2:-3]
                procArr.append((int(pID), return_val))

    f.close()

    return procArr


if __name__ == '__main__':
    pArr = getProcesses()
    print(pArr)