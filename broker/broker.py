import socket
import landerdb
import threading
import thread
import time
import json

class Broker:
    def __init__(self):
        self.sock = socket.socket()
        self.db = landerdb.Connect("nodes.db")
        self.port = 3333
        self.host = "0.0.0.0"

    def main(self):
       self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       self.sock.bind((self.host, self.port))
       self.sock.listen(5)
       while True:
            obj, ip = self.sock.accept()
            threading.Thread(target=self.handle, args=(obj,ip[0])).start()
    
    def handle(self, obj, ip):
        try:
            data = json.loads(obj.recv(1024000))
            print data
        except:
            return
        else:
            if "port" in data and "id" in data and "relay" in data:
                if data['relay'] == True:
                    self.db.insert("nodes", {"port":data['port'], "ip":ip, "id":data['id']})
            with open("nodes.db", 'rb') as file:
                obj.send(file.read())
            obj.close()

    def check(self):
        while True:
            data = self.db.find("nodes", "all")
            for x in data:
                ip = x['ip']
                port = x['port']
                s = socket.socket()
                try:
                    s.settimeout(1)
                    s.connect((ip, port))
                except:
                    self.db.remove("nodes", {"id":x['id']})
                    s.close()
                    continue
                else:
                    s.send(json.dumps({"cmd":"ping"}))
                    data = s.recv(1024)
                    if data:
                        continue
                    else:
                        self.db.remove("nodes", {"id":x['id']})
            time.sleep(60)

if __name__ == "__main__":
    thread.start_new_thread(Broker().check, ())
    Broker().main()

