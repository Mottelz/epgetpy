import requests, json, os

def getToken():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', }
    data = '{  "apikey": "B4AAF3CDC8191A8A",  "userkey": "9E37DA78322F6E6A",  "username": "mottelz" }'
    response = requests.post('https://api.thetvdb.com/login', headers=headers, data=data)
    token = json.loads(response.content)['token']
    return token


def getShowID(token, showName):
    headers = {'Accept': 'application/json','Authorization': 'Bearer '+token}
    params = (('name', showName),)
    response = requests.get('https://api.thetvdb.com/search/series', headers=headers, params=params)
    fulllist = json.loads(response.content)['data']
    count=0
    for x in fulllist:
        print(str(count)+': '+x['firstAired']+' '+str(x['id'])+' '+x['seriesName'])
        count+=1
    choice = int(input('Choose one: '))
    return str(fulllist[choice]['id'])


def getSeasonData(token, showid, season):
    headers = {'Accept': 'application/json','Authorization': 'Bearer '+token,}
    response = requests.get('https://api.thetvdb.com/series/'+showid+'/episodes/query?airedSeason='+season, headers=headers)
    return json.loads(response.content)['data']


def dataToFilenames(data):
    toReturn = []
    for x in data:
        if x['episodeName'] is None:
            break
        if x['airedEpisodeNumber'] < 10:
            toReturn.append(str(x['airedSeason']) +'0'+ str(x['airedEpisodeNumber'])+' '+x['episodeName'])
        else:
            toReturn.append(str(x['airedSeason']) + str(x['airedEpisodeNumber'])+' '+x['episodeName'])
    return toReturn


def renameFiles(newNames, filepath, extension):
    count = 0
    for file in sorted(os.listdir(filepath)):
        if file.endswith(extension):
            print('Renaming: '+file+' to '+newNames[count]+extension)
            os.rename(src=filepath+file, dst=filepath+newNames[count]+extension)
            count = count+1

