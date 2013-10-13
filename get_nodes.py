import socket
import data
import json

def get_nodes_send(obj, data):
    with open("nodes.db", 'rb') as file:
        obj.send(file.read())

def get_nodes():
    lis = data.config['db'].find("nodes", "all")
    if not lis:
        data.config['db'].insert("nodes", {})
        data.config['db'].remove("nodes", {})
        lis = data.config['db'].find("nodes", "all")
    for x in lis:
        s = socket.socket()
        try:
            s.settimeout(1)
            s.connect((x['ip'], x['port']))
        except:
            continue
        else:
            s.send(json.dumps({"cmd":"get_nodes"}))
            data_ = s.recv(1024000)
            with open("nodes.db", 'wb') as file:
                file.write(data_)
            break

