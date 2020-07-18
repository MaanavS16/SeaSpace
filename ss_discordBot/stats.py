import meteomatics.api as api

import json
import requests

class Stats:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_temp(self, x, y):
        try:
            res = api.query_api("https://api.meteomatics.com/now/t_0m:C/{},{}/json".format(x, y), self.username, self.password)
        except Exception as e:
            print("Failed, the exception is {}".format(e))
        print(res.headers)
        print(res.content)
        return res.json()['data'][0]['coordinates'][0]['dates'][0]['value']

    def get_salinity(self, x, y):
        try:
            res = api.query_api("https://api.meteomatics.com/now/salinity:psu/{},{}/json".format(x, y), self.username, self.password)
        except Exception as e:
            print("Failed, the exception is {}".format(e))
        print(res.headers)
        print(res.content)
        return res.json()['data'][0]['coordinates'][0]['dates'][0]['value']
    def get_depth(self, x, y):
        try:
            res = api.query_api("https://api.meteomatics.com/now/ocean_depth:km/{},{}/json".format(x, y), self.username, self.password)
        except Exception as e:
            print("Failed, the exception is {}".format(e))
        print(res.headers)
        print(res.content)

        return res.json()['data'][0]['coordinates'][0]['dates'][0]['value']

x = Stats()
y = x.get_temp(0,0)
print(y)
