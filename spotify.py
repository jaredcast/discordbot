from info import *

'''results = sp.search(q='Bladee', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['uri'])

def artist_info(artist):
    results = sp.search(q=artist, limit=20)
'''

#https://developer.spotify.com/documentation/web-api/reference/albums/get-album/
results = sp.search(q='Bladee',  limit=20)
'''print(results['tracks'])
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['type'])'''

print(results)
'''for x in results['tracks']['items']:
    print(x['album']['name'])'''


'''for x in results['tracks']:
    print(x)''' #Dummy code for showing what we can search with

for x in results['tracks']['items']: #Returns various dictionaries, the list of all objects.. This documents album object https://developer.spotify.com/documentation/web-api/reference/albums/get-album/
    print(x['album']["album_type"])