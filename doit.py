import socket

def doit(host, data):
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
