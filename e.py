import win32gui
import win32process
import wmi
import win32api
import time
import psutil
from pywintypes import error
import random
import threading as th
from colored import fg
from os import system
system("title " +"  " )

color = fg('deep_sky_blue_4a')
mc = 0
c = wmi.WMI()
a = input()
if a != "cyroop":
    self.e

def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
    try:
        return psutil.Process(pid[-1]).name()
    except:
        return ""

def get_app_path(hwnd):
    """Get applicatin path given hwnd."""
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in c.query('SELECT ExecutablePath FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
            exe = p.ExecutablePath
            break
    except:
        return None
    else:
        return exe


def get_app_name(hwnd):
    """Get applicatin filename given hwnd."""
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
            exe = p.Name
            break
    except:
        return None
    else:
        return exe


target_found = False

def enumHandler(hwnd, lParam):
    
    global target_found
    
    if not target_found:
        
        if str((get_app_name(hwnd))) == "javaw.exe":
            global mc
            mc = hwnd

            target_found = True
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
if checkIfProcessRunning('anydesk'):
    self.e
                 
print(fg('deep_sky_blue_4b') + 
r"""   ___                           __   _   _          
  / __\  _   _ _ __    ___      / /  (_) | |_    ___ 
 / /    | | | | '__|  / _ \    / /   | | | __|  / _ \
/ /___  | |_| | |    | (_) |  / /___ | | | |_  |  __/
\____/   \__, |_|     \___/   \____/ |_|  \__|  \___|
         |___/                                       """)
            
print(fg('deep_sky_blue_4b') + r"The first python clicker")
cps=input(fg('deep_sky_blue_4c')+"cps? ")


delay = 1/int(cps) - 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
if int(cps) > 10:
    delay = delay-0.021

randomize = random.randint(-6,6)

randomize=0
posorneg = randomize=random.randint(0,1)
win32gui.EnumWindows(enumHandler, None)
while True:
    randomize = random.randint(-6,6)
    cpss = int(cps) + randomize
    delay = 1/int(cpss) - 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001

    if active_window_process_name() == "javaw.exe":
        run =1
    if active_window_process_name() != "javaw.exe":
        run = 0
    if run == 1:
        try:
            mouse = win32api.GetAsyncKeyState(0x01)
            if mouse < 0 :
                win32api.PostMessage(mc, 0x0201, 0, 0)
                time.sleep(0.000000000000000000001/9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
                win32api.PostMessage(mc, 0x0202, 0, 0)
                if int(cps) > 12:
                    time.sleep(delay-0.02)
                else:
                    time.sleep(delay)

        except error:
            target_found=False
            win32gui.EnumWindows(enumHandler, None)

