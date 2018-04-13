import requests
import json

def getToken():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', }
    data = '{  "apikey": "B4AAF3CDC8191A8A",  "userkey": "9E37DA78322F6E6A",  "username": "mottelz"}'
    response = requests.post('https://api.thetvdb.com/login', headers=headers, data=data)
    token = json.loads(response.content)['token']
    return token


def getSeasonData(token, showid, season):
    headers = {'Accept': 'application/json','Authorization': 'Bearer '+token,}
    response = requests.get('https://api.thetvdb.com/series/'+showid+'/episodes/query?airedSeason='+season, headers=headers)
    return json.loads(response.content)['data']


token = getToken()
print(getSeasonData(token, '277928', '4'))