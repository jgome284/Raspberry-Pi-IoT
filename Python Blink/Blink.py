#import libraries
import RPi.GPIO as GPIO
import time
import os

#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#counter
i = 0
t = int(input("How many seconds would you like this program to run? "))

#blink interval
b = float(input("How many seconds would you like the blink period to be? "))

#adjust time
t = t/b

#run
while i < t:
    i = i + 1
    print(i*b)
    if GPIO.input(16):
          GPIO.output(12,GPIO.HIGH)
          time.sleep(b)
    else:
          GPIO.output(12,GPIO.HIGH)
          time.sleep(b/2)
          GPIO.output(12,GPIO.LOW)
          time.sleep(b/2)
GPIO.cleanup()

os.system('clear')
    
    
