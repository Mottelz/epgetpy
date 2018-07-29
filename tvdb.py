import requests, json, os


# Grabs the token
def getToken():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', }
    data = '{  "apikey": "8OLZK9HOF5D65PX4",  "userkey": "9E37DA78322F6E6A",  "username": "mottelz" }'
    response = requests.post('https://api.thetvdb.com/login', headers=headers, data=data)
    token = json.loads(response.content)['token']
    return token


# Uses query to get the show ID
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


# Uses the show ID to get the raw season data
def getSeasonData(token, showid, season):
    headers = {'Accept': 'application/json','Authorization': 'Bearer '+token,}
    response = requests.get('https://api.thetvdb.com/series/'+showid+'/episodes/query?airedSeason='+season, headers=headers)
    return json.loads(response.content)['data']


# Converts the raw data to file names
def dataToFilenames(data):
    toReturn = []
    for x in data:
        if x['episodeName'] is None:  # Here because sometimes later episodes do not have or there is a blank episode
            continue
        if x['airedEpisodeNumber'] < 10:
            toReturn.append(str(x['airedSeason']) +'0'+ str(x['airedEpisodeNumber'])+' '+x['episodeName'])
        else:
            toReturn.append(str(x['airedSeason']) + str(x['airedEpisodeNumber'])+' '+x['episodeName'])
    return sorted(toReturn)


# Renames the files
def renameFiles(newNames, filepath, extension):
    for file in os.listdir(filepath):
        os.rename(src=filepath + file, dst=filepath + file.lower())
    count = 0
    for file in sorted(os.listdir(filepath)):
        if file.endswith(extension):
            print('Renaming: '+file+' to '+newNames[count]+extension)
            os.rename(src=filepath+file, dst=filepath+newNames[count]+extension)
            count = count+1

