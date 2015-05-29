#!/usr/bin/python3
__author__ = 'zhangcheng'

import requests
import json

def cut(text):
    url = "http://localhost:5080/"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "cut",
        "params": text,
        "jsonrpc": "2.0",
        "id": "0",
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    return response['result']

if __name__ == "__main__":
    while True:
        str = input("To cut:");
        print(cut(str+'\n'+str));
