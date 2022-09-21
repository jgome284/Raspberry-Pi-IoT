import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind() binds the socket to a port, 1234 is a generic port, a web server is port 80, "" is an empty host
mysock.bind(("",1234))

#listen() starts listening for a connect(), the argument is the backlog, or number of requests allowed to wait for service
mysock.listen(5)

#accept() accepts a connection request... it returns two things: a connection (for sending/receiving) and an address (IP,port)
conn, addr = mysock.accept()
