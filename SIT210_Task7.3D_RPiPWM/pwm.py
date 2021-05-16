from gpiozero import DistanceSensor, Buzzer
import RPi.GPIO as GPIO
from time import sleep

triggerPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)

buzzer = GPIO.PWM(triggerPin, 1000)
buzzer.start(10)

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)

while True:
  if ultrasonic.distance < 1:
    duty = 10 / ultrasonic.distance 
    buzzer.ChangeDutyCycle(duty)
    sleep(0.5)
  else:
    buzzer.ChangeDutyCycle(0)
    sleep(0.5)

