import socket
import threading
import thread
import data
import ping
import get_nodes_broker
import os
import get_nodes
import json
import time
import proxy

class Karat:
    def __init__(self):
        self.data = data.config
        self.cmds = {
            "ping":ping.pong,
            "get_nodes":get_nodes.get_nodes_send,
            "proxy":proxy.proxify,
        }

    def main(self):
        thread.start_new_thread(self.getem, ())
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((data.config['host'], data.config['port']))
        self.sock.listen(5)
        while True:
            obj, ip = self.sock.accept()
            threading.Thread(target=self.handle, args=(obj, ip[0])).start()

    def handle(self, obj, ip):
        data_ = obj.recv(1024000)
        try:
            data_ = json.loads(data_)
        except:
            proxy.proxy(obj, data_)
        else:
            print ip+": "+str(data_)
            if "cmd" in data_:
                if data_['cmd'] in self.cmds:
                    self.cmds[data_['cmd']](obj, data_)

    def getem(self):
        while True:
            try:
                if not data.config['db'].find("nodes", "all"):
                    get_nodes_broker.get_nodes()                                                                                                       
                else:
                    get_nodes.get_nodes()
                time.sleep(10)
            except ValueError:
                with open("nodes.db", 'wb') as file:
                    file.write("{}")

if __name__ == "__main__":
    try:
        Karat().main()
    except KeyboardInterrupt:
        exit()
