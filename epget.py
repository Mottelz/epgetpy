#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import tvdb

token = tvdb.getToken()
seriesID = tvdb.getShowID(token, input('Enter show name: '))
data = tvdb.getSeasonData(token, seriesID, input('Enter season: '))
episodes = tvdb.dataToFilenames(data)
if (input('Do you want to rename files?')) == 'y':
    filepath = input('Input file path: ')
    ext = input('Input file extension: ')
    tvdb.renameFiles(episodes, filepath, ext)
else:
    for name in episodes:
        print(name)
