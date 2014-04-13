import requests
import sys
import json

API_Root="https://api.pinocc.io/v1/"
token = "<your api key here!>"
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
    received = 0
    r = get("sync",stream=True)
    print r.status_code
    for line in r.iter_lines(chunk_size=1): 
        received = received + 1 
        if line: 
            print "({}) {}".format(received, json.loads(line))
        else:
            print "({}) keepalive".format(received) 
