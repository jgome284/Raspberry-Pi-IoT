import socket
import picamera
import time

mysocket = socket.socket()

mysocket.connect(('',8000))

#need a file like object to capture to
conn = mysocket.makefile('wb')
camera.capture(conn, 'jpeg')
