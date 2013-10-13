import data
import socket
import json

def get_nodes():
    s = socket.socket()
    try:
        s.connect(data.config['broker'])
    except Exception, e:
        print "Could not connect to broker."
    else:
        s.send(json.dumps({"port":data.config['port'], "id":data.config['id'], "relay":data.config['relay']}))
        data_ = s.recv(1024000)
        if not data:
            get_nodes()
        with open("nodes.db", 'wb') as file:
            file.write(data_)
