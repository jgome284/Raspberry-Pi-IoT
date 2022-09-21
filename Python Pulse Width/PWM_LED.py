#import libraries
import RPi.GPIO as GPIO
import time
import os

#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)


pwm12 = GPIO.PWM(12, 50)
pwm12.start(0)

try:
  while True:
    for dutyCycle in range (0, 100, 5):
      pwm12.ChangeDutyCycle(dutyCycle)
      time.sleep(0.1)

    for dutyCycle in range (100, 0, -5):
      pwm12.ChangeDutyCycle(dutyCycle)
      time.sleep(0.1)

except KeyboardInterrupt:
  pwm12.stop()

GPIO.cleanup()

os.system('clear')
    
    

