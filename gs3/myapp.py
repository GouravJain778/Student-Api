import requests
import json
URL="http://127.0.0.1:8004/get/"
def get_data(id=None):
    data={}
    if id is not None:
        data = {"id":id}
    jason_data=json.dumps(data)
    print("oututtt",jason_data)
    r=requests.get(url=URL,data=jason_data)
    result=r.json()
    print(result)
    
# get_data()

def post_data():
    data={ 

        
        'name':'rohit',
        'roll':127,
        'city':'chhatarpur'
    }
    
    jason_data=json.dumps(data)
    r=requests.post(url=URL,data=jason_data)
    data=r.json()
    print(data)
post_data()

def update_data():
    data={ 

        'id':2,
        'name':'mayankjain',

        'city':'bang'
    }
    
    jason_data=json.dumps(data)
    r=requests.put(url=URL,data=jason_data)
    data=r.json()
    print(data)
# update_data()
def delete_data():
    data={ 

        'id':4
    }
    
    jason_data=json.dumps(data)
    r=requests.delete(url=URL,data=jason_data)
    data=r.json()
    print(data)
# delete_data()

