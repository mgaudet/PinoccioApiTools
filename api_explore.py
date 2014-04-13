import requests
import sys

API_Root="https://api.pinocc.io/v1/"
token = "<your API key here>"
auth_arg = {"token" : token} 

def get(url, **kwargs): 
    """
    Issue a get request to the Pinnocio API, authenticated by the token
    """
    if "data" in kwargs: 
        kwargs["data"] = dict(kwargs["data"].items() + auth_arg.items())
    else:
        kwargs["data"] = auth_arg
    return requests.get(API_Root + url, **kwargs)


if __name__  == '__main__': 
    if len(sys.argv) > 1: 
        r = get(sys.argv[1])
        print r.status_code
        print r.text
    else:
        print "Need a command" 

