import Rpi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12,50)
pwm.start(0)

for i in range(10):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.1)
for i in range(10, 0, -1):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.1)