import socket
import sys

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
conn, addr = mysock.accept()
print("Got a Request!")

while True:
    
    data = conn.recv(1000)
    if not data:
        break
    elif data == b'Exit\n':
        break
    else:
        print(data.decode())

#close both the client connection and server socket
print("Connection Closed")
conn.close()
mysock.close()