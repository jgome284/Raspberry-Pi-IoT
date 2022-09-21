import socket
#AF_INET sets socke to internet connection
#SOCK_STREAM sets socket to TCP (connection based)
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("This is my socket: ", mysock)

#gethostbyname() is a library module that derives the website ip address through the DNS server
host = socket.gethostbyname("www.youtube.com")
print("This is the host: ", host)

#connect() creates the connection to the host, port 80 is the standard web server port 
mysock.connect((host,80))

#Send an HTTP GET Request
message = "GET / HTTP/1.1\r\n\r\n"
print(message)

#sendall() sends data to the server and tries until it succeeds
#.encode() converts the message string into bytes so that the message can be transfered through the socket
mysock.sendall(message.encode())

#recv() returns data on the socket, 1000 is the maximum number of bytes you expect to receive
data = mysock.recv(1000) 
print(data.decode())

#close() closes the socket connection so it can be reused later
mysock.close()