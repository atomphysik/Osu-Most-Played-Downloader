import json
import requests
import os
import string
import unicodedata
import time


validFilenameChars = "-_.() %s%s" % (string.ascii_letters, string.digits)
def removeDisallowedFilenameChars(filename):
    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return ''.join(chr(c) for c in cleanedFilename if chr(c) in validFilenameChars)

user_id = int(input('Enter User ID from profile URL: '))
number_of_maps = int(input('Enter top number of maps to download: '))

print('\nThere will be a 2 second delay between each download to prevent error for too many requests')

beatmap_id_set = set() # set used to keep track of downloaded beatmaps
beatmap_count = 0

offset = 0

while(number_of_maps > 0):
    
    r = requests.get(f'https://osu.ppy.sh/users/{user_id}/beatmapsets/most_played?offset={offset}&limit={number_of_maps}')
    data = r.json()
    
    try:
        os.makedirs("./songs")
    except FileExistsError:
        pass

    for beatmap in data:

        beatmap_count += 1

        beatmap_id = beatmap['beatmapset']['id']
        beatmap_artist = removeDisallowedFilenameChars(str(beatmap['beatmapset']['artist']))
        beatmap_title = removeDisallowedFilenameChars(str(beatmap['beatmapset']['title']))

        if beatmap_id in beatmap_id_set:
            print(f'\nSkipping duplicate --> {beatmap_count}. {beatmap_title}')
            continue
        else:
            beatmap_id_set.add(beatmap_id)

        if beatmap_count != 1 : time.sleep(2) # delay put to prevent error 429, delay skipped for the first download

        download_url = f"https://beatconnect.io/b/{beatmap_id}/"
        
        print(f'\n-------{beatmap_id}-------')
        print(download_url)
        print(f'ssibal download joong: {beatmap_count}. ' + str(beatmap_title))
        
        r = requests.get(download_url)
        headers = r.headers
        file_size = int(headers.get('Content-Length'))
        
        if file_size < 10000:
            print('cannot connect to bc server or beatmap does not exist in bc')
            bye = ""
            while(bye != "y" and bye != "Y" and bye != "n" and bye != "N") :
                bye = str(input('Do you wanna continue downloading? y/n: '))
                if bye == "y" or bye == "Y" :
                    quit()
                elif bye == "n" or bye == "N" :
                    with open(f'./songs/{beatmap_id} {beatmap_title}.osz', 'wb') as f:  
                        f.write(r.content)
        else :
            with open(f'./songs/{beatmap_id} {beatmap_artist} - {beatmap_title}.osz', 'wb') as f:  
                f.write(r.content)

        

    
    number_of_maps -= 51 # number of maps left
    offset += 51 # site only allows 51 downloads each request
