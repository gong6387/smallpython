import win32api
import win32con
import win32gui
from ctypes import *
import time

def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.008)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)

def t0():
    pass
def t1():
    nn = [9 for x in range(0, 75)]
    i,j = 0,0
    w,h = 1170,520
    width = 460
    for n in range(len(nn)):
        i = 0
        while i <= nn[n]:
            j = 0
            while j <= nn[n]:
                mouse_click(w+width/nn[n]*i,h+width/nn[n]*j)
                j = j+1
            i = i+1
            

if __name__ == "__main__":
    t1()
    t0()
