#import libraries
import RPi.GPIO as GPIO
import time

#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


#run
print ("on")
GPIO.output(18,GPIO.HIGH)
time.sleep(2)
print ("off")
GPIO.output(18,GPIO.LOW)
time.sleep(2)
print ("<**>")

