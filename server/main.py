from fastapi import FastAPI, HTTPException
from server.api import Api

server_api = Api()
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome"}

@app.get("/get_value/")
def get_value(key):
    res = server_api.get_value_by_key(key)
    if res == None:
        raise HTTPException(status_code=404, \
            detail={'status': 'failure', 'msg': 'key not found!', 'type': 'value'})
    return {'status': 'success', 'key': key, 'value': res, 'type': 'value'}

@app.get("/history/", status_code=200)
def get_history(key):
    res = server_api.get_history(key)
    if res == None:
        raise HTTPException(status_code=404, \
            detail={'status': 'failure', 'msg': 'key not found!', 'type': 'history'})
    return {'status': 'success', 'key': key, 'history': res, 'type': 'history'}

@app.post("/set/", status_code=201)
def set_value(key, value):
    res = ""
    if server_api.contains_key(key):
        out = server_api.update_key_value(key, value)
        res = {'status': 'success', 'msg': out, 'type': 'update'}
    else:
        out = server_api.create_key_value(key, value)
        res = {'status': 'success', 'msg': out, 'type': 'create'}
    return res