from tkinter import *
import tkinter.font

from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


def ledToggle1():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(10, GPIO.LOW)

def ledToggle2():
    GPIO.output(12, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)

def ledToggle3():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(16, GPIO.LOW)

def close():
  GPIO.cleanup()
  win.destroy()


ledButton1 = Button(win, text = "Toggle LED1", font = myFont, command = ledToggle1, bg = "bisque2", height = 1, width = 24)
ledButton1.grid(row=0, column = 1)

ledButton2 = Button(win, text = "Toggle LED2", font = myFont, command = ledToggle2, bg = "bisque2", height = 1, width = 24)
ledButton2.grid(row=1, column = 1)

ledButton3 = Button(win, text = "Toggle LED3", font = myFont, command = ledToggle3, bg = "bisque2", height = 1, width = 24)
ledButton3.grid(row=2, column = 1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
