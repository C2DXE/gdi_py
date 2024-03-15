from win32gui import *
from win32api import *
from win32file import *
from win32ui import *
from win32con import *
from random import *
import ctypes
import win32gui
import win32con
import math
import time
import random
import win32api
import advancedpythonmalware

def gdicolor(time,repeat):
    desktop = GetDC(0)
    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    for i in range(repeat):
    
        brush=CreateSolidBrush(RGB(
            randint(0,255),
            randint(0,255),
            randint(0,255),
    ))
        SelectObject(desktop,brush)
        PatBlt(desktop,0,0,x,y, PATINVERT)
        Sleep(time)
        PatBlt(desktop,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
        Sleep(time)
        PatBlt(desktop,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
        Sleep(time)
        DeleteObject(brush)
    ReleaseDC(desktop,GetDesktopWindow())
    DeleteDC(desktop)

def gdiblackwhite(time,repeat):
    for i in range(repeat):
        desktop = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        brush=CreateSolidBrush(RGB(
            randint(0,255),
            randint(0,255),
            randint(0,255),
        ))
        SelectObject(desktop,brush)
        PatBlt(desktop,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
        Sleep(time)
        PatBlt(desktop,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)


def invert(time):
    hdc = win32gui.GetDC(0)
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    for i in range(time):
        win32gui.InvertRect(hdc, (0, 0, w ,h))

def errorscreen(time,repeat):
    ##recomendado (500,500) porque sino es muy corto
    hdc = win32gui.GetDC(0)
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    x = y = 0
    for i in range(repeat):
        for i in range(time):
            win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR)) # Change IDI_ERROR to something else to change the icon being displayed
            x = x + 30
            if x >= w:
                y = y + 30
                x = 0
            if y >= h:
                x = y = 0

def panscreen(times):
    ##recomendado 200-500
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = win32gui.GetDC(0)
    dx = dy = 1
    angle = 0
    size = 1
    speed = 5
    for i in range (times):
    
        win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
        dx = math.ceil(math.sin(angle) * size * 10)
        dy = math.ceil(math.cos(angle) * size * 10)
        angle += speed / 10
        if angle > math.pi :
            angle = math.pi * -1

def waves(times):
    #recomendado 2-5
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    angle = 0

    for i in range(times):
        hdc = win32gui.GetWindowDC(desktop)
        for i in range(int(sw + sh)):
            a = int(math.sin(angle) * 20)
            win32gui.BitBlt(hdc, 0, i, sw, 1, hdc, a, i, win32con.SRCCOPY)
            angle += math.pi / 40
        win32gui.ReleaseDC(desktop, hdc)
        time.sleep(0.01)

def rainbowhell(times):
    ##recomendado 200-500
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    for i in range(times):
        hdc = win32gui.GetDC(0)
        color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
        brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
        win32gui.SelectObject(hdc, brush)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)

def bwhell(times):
    ##lo mismo que el rainbowhell
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = win32gui.GetDC(0)
    for i in range(times):
    
        win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -3,-3, win32con.NOTSRCCOPY)


