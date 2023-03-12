import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)

# get_data()

# for POST METHOD
def post_data():
    data = {
        'name':'ravi',
        'roll':104,
        'city':'dhanbad'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

def update_data():
    data = {
        'id':4,
        'name':'rohit',
        'roll':104,
        'city':'dhanbad'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data=r.json() # the 'msg' will be returned and stored in r, which will then be converted
    print(data)

# update_data()
# post_data()

def delete_data():
    data = {
        'id':5
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data=r.json() # the 'msg' will be returned and stored in r, which will then be converted
    print(data)

delete_data()