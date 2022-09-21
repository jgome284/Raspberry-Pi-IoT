import socket
import sys
import RPi.GPIO as GPIO

#create socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#bind() binds the socket to a port, 1234 is a generic port, a web server is port 80, "" is an empty host
try:
    mysock.bind(("",1234))
except socket.error:
    print("Failed to bind")
    sys.exit()

#listen() starts listening for a connect(), the argument is the backlog, or number of requests allowed to wait for service
mysock.listen(5)

#accept() accepts a connection request... it returns two things: a connection (for sending/receiving) and an address (IP,port)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    #to turn the string into a byte array is placing a b in front. For example b' '.
    if data == b'on':
        GPIO.output(13,True)
        print("LED turned on")
    if data == b'off':
        GPIO.output(13,False)
        print("LED turned off")
        
#close both the client connection and server socket
conn.close()
mysock.close()