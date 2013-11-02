#import socket
import httplib
from urlparse import urlparse
def doit(host, data):
    
    data = data.replace("\r", '')
    http = httplib.HTTPConnection(host)
    data = data.split("\n")
    main = data[0].split()
    type_ = main[0]
    url = main[1]
    out = urlparse(url)
    headers = {}
    for x in data[2:]:
        x = x.split(":")
        try:
            headers[x[0]] = x[1]
        except:
            continue
    http.request(type_, out[2], out[4], headers)
    data = http.getresponse()
    return data.read()

    """
    s = socket.socket()
    host = host.split()[0]
    s.connect((host, 80))
    s.send(data)
    data = s.recv(1024000)
    if data:
        s.close()
        return data
    else:
        s.close()
        return "Something went wrong."
    """
