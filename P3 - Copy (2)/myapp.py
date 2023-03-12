import requests
import json

URL = "http://127.0.0.1:8000/studentapiclass/"
# URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)



# for POST METHOD
def post_data():
    data = {
        'name':'abd',
        'roll':17,
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

def delete_data():
    data = {
        'id':4
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data=r.json() # the 'msg' will be returned and stored in r, which will then be converted
    print(data)

# get_data()
post_data()
# update_data()
# delete_data()