import requests
import sys

API_Root="https://api.pinocc.io/v1/"
token = "<your api key here>"
auth_arg = {"token" : token} 

def get_token(username, password): 
    pass

def get(url, **kwargs): 
    if "data" in kwargs: 
        kwargs["data"] = dict(kwargs["data"].items() + auth_arg.items())
    else:
        kwargs["data"] = auth_arg
    return requests.get(API_Root + url, **kwargs)

if __name__  == '__main__': 
    if len(sys.argv) > 3: 
        command = " ".join(sys.argv[3:])
        r = get("{}/{}/command/".format(sys.argv[1],sys.argv[2]),data={"command": command}) 
        print r.status_code
        print r.text
    else:
        print "Need a troop, a scout, and a command" 

