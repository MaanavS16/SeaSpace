import meteomatics.api as api
import json
import requests
import datetime as dt

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
    def get_temp_pic(self, x, y):
        filename_png = 'temp_pic.png'
        startdate_png = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        parameter_png = 't_2m:C'
        lat_N = y + 15
        lon_W = x - 15
        lat_S = y - 15
        lon_E = x + 15
        res_lat = 0.01
        res_lon = 0.01
        print("grid as a png:")
        try:
            api.query_grid_png(filename_png, startdate_png, parameter_png, lat_N, lon_W, lat_S, lon_E, res_lat, res_lon,
                               self.username, self.password)
            print("filename = {}".format(filename_png))
        except Exception as e:
            print("Failed, the exception is {}".format(e))
    
