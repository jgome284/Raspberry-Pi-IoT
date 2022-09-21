import http.client

conn = http.client.HTTPSConnection("www.uci.edu")
conn.request("GET", "/")
r1 = conn.getresponse()
while chunk := r1.read(200):
    print(repr(chunk))
    