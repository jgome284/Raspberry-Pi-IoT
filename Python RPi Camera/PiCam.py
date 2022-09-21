import picamera
import time

#instantiate an object of the PiCamera class
camera = picamera.PiCamera()

#Take a Picture
camera.capture("pict.jpg")

#Camera Functions
camera.hflip = True
camera.vflip = True
camera.brightness = 50
camera.sharpness = 0

#Preview Video
camera.start_preview()
camera.stop_preview()

#Video Recording

camera.start_recording("vid.h264")
time.sleep(10)
camera.stop_recording()
