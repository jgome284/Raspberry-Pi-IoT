'''
Let's do a timelapse photography program!
'''

import picamera
import time
#iterate through all the images
#5 minute delay

camera = picamera.PiCamera()
for filename in camera.capture_continuous('picture{counter}.jpg'):
    time.sleep(300)

    
    
