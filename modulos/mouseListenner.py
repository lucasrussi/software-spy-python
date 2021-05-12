from pynput import mouse
from win32gui import GetWindowText, GetForegroundWindow

def on_click(x,y,button,pressed):
    stringWindows = str(GetWindowText(GetForegroundWindow())).lower()
    stringWindows.lower()
    with open('logFile.txt', 'a')  as f:
        for string in stringWindows:
            f.write(stringWindows + '\n')
    


with mouse.Listener(
    on_click=on_click
) as listener:
    listener.join()

on_click_save = on_click()