import http.client
conn = httplib.HTTPConnection("www.google.com")
conn.request("GET","/")