import data
import json

def pong(obj, data):
    obj.send(json.loads({"cmd":"PONG"}))
