import urllib3
import json
import re

http = urllib3.PoolManager()
host = "127.0.0.1"
port = 8000
URL = f"http://{host}:{port}"

def cli_handler():
    command = ""
    while True:
        command = input()
        parts = re.split("\s+", command)
        if parts[0] == "set":
            print(set_key_value(parts[1], parts[2]))
        elif parts[0] == "get":
            print(get_value(parts[1]))
        elif parts[0] == "history":
            print(get_history(parts[1]))
        elif parts[0] == "quit":
            break
        else:
            print("Please enter a valid command.")
            
def set_key_value(key, value):
    try:
        r = http.request('POST', URL+f"/set/?key={key}&value={value}")
        r_json = json.loads(r.data)
        if r.status == 201:
            return r_json['msg']
        else:
            return "error."
    except:
        return "Please run the server on 127.0.0.1:8000"

def get_value(key):
    try:
        r = http.request('GET', URL+f"/get_value/?key={key}")
        r_json = json.loads(r.data)
        if r.status == 200:
            return f"value for key {r_json['key']} is {r_json['value']}"
        elif r.status == 404:
            return r_json['detail']['msg']
        else:
            return "error."
    except:
        return "Please run the server on 127.0.0.1:8000"

def get_history(key):
    try:
        r = http.request('GET', URL+f"/history/?key={key}")
        r_json = json.loads(r.data)
        if r.status == 200:
            return f"history of {r_json['key']} is {r_json['history']}"
        elif r.status == 404:
            return r_json['detail']['msg']
        else:
            return "error."
    except:
        return "Please run the server on 127.0.0.1:8000"

if __name__ == "__main__":
    print("Hi, welcome\nPlease Enter a command in one of these forms:\n\
        1.set key1 value1\n\
        2.get key1\n\
        3.history key1\n\
        4.quit")
    cli_handler()
