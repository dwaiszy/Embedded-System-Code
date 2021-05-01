from tkinter import *
import tkinter.font
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

win = Tk()
win.title('Morse LED')
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

letters = {
      'A': '.-', 
      'B': '-...', 
      'C': '-.-.', 
      'D': '-..', 
      'E': '.', 
      'F': '..-.', 
      'G': '--.', 
      'H': '....', 
      'I': '..', 
      'J': '.---', 
      'K': '-.-', 
      'L': '.-..', 
      'M': '--', 
      'N': '-.', 
      'O': '---', 
      'P': '.--.', 
      'Q': '--.-', 
      'R': '.-.', 
      'S': '...', 
      'T': '-', 
      'U': '..-', 
      'V': '...-', 
      'W': '.--', 
      'X': '-..-', 
      'Y': '-.--', 
      'Z': '--..', 
      '1': '.----', 
      '2': '..---', 
      '3': '...--', 
      '4': '....-', 
      '5': '.....', 
      '6': '-....', 
      '7': '--...', 
      '8': '---..', 
      '9': '----.', 
      '0': '-----', 
      ' ': '/'
}

def morseBlink():
    _input = input.get()
    word = list(_input.upper())

    for letter in word:
        time.sleep(2)
        character = letters[letter]
        print(character)

        for code in character:
            if code == '=':
                ledControl(0.5)
            elif code == '.':
                ledControl(0.2)
            elif code == '/':
                time.sleep(1)

def ledControl(time_sleep):
    GPIO.output(10, GPIO.HIGH)
    time.sleep(time_sleep)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.5)

def close():
    GPIO.cleanup()
    win.destroy()

input = tkinter.Entry(win)

input.grid(row=0, column=1)

button = Button(win, text = 'Blink', font = myFont, command = morseBlink, bg = 'bisque2', height = 1, width = 24)
button.grid(row=1, column=1)

win.protocol('WM_DELETE_WINDOW', close)
win.mainloop()
