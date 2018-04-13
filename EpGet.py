import requests
import json

headers = {'Content-Type': 'application/json','Accept': 'application/json',}

data = '{  "apikey": "B4AAF3CDC8191A8A",  "userkey": "9E37DA78322F6E6A",  "username": "mottelz"}'

response = requests.post('https://api.thetvdb.com/login', headers=headers, data=data)

token = json.loads(response.content)
