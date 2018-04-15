#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import tvdb

token = tvdb.getToken()  # Get the token.
seriesID = tvdb.getShowID(token, input('Enter show name: '))  # Get the show ID.
data = tvdb.getSeasonData(token, seriesID, input('Enter season: '))  # Grab the list of episodes (raw data).
episodes = tvdb.dataToFilenames(data)  # Convert the raw data to preferred style.
if (input('Do you want to rename files? "y" for yes.')) == 'y':  # Decide to rename or print to screen.
    filepath = input('Input file path: ')  # Get the file path.
    ext = input('Input file extension: ')  # Get the file extension.
    tvdb.renameFiles(episodes, filepath, ext)  # Rename the files.
else:
    for name in episodes:  # Print the data to screen.
        print(name)
