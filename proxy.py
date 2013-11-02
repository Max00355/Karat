import socket
import data as db
import random
import json
import re
import doit

def proxy(obj, data):
    
    check = db.config['db'].find("nodes", "all") 
    node = random.choice(check)
    s = socket.socket()
    try:
        s.connect((node['ip'], node['port']))
    except:
        s.close()
    else:
        s.send(json.dumps({"cmd":"proxy", "data":data}))
        data = s.recv(1024000)
        obj.send(data)
        obj.close()
        

def proxify(obj, data):
    host = re.findall("Host: (.*)", data['data'])[0]
    do = doit.doit(host.split()[0], data['data'])
    obj.send(do)
    obj.close()

