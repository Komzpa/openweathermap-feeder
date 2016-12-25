import config
import requests

def feed_measurement(data):
    url = "http://api.openweathermap.org/data/3.0/measurements?appid=%s" % config.apikey
    req = requests.post(url, json=data)
    print(req)
