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


def dataToFilenames(data, extension):
    toReturn = []
    for x in data:
        if x['airedEpisodeNumber'] < 10:
            toReturn.append(str(x['airedSeason']) +'0'+ str(x['airedEpisodeNumber'])+' '+x['episodeName']+extension)
        else:
            toReturn.append(str(x['airedSeason']) + str(x['airedEpisodeNumber'])+' '+x['episodeName']+extension)
    return toReturn


token = getToken()
data = getSeasonData(token, '277928', '4')
ext = '.mkv'
print(dataToFilenames(data, ext))