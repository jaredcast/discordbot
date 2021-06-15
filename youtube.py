import os

import googleapiclient.discovery
import googleapiclient.errors
from info import ytkey

def ytSearch(keyword):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=ytkey)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q = keyword
    )
    response = request.execute()
    #print(response['items'])
    result = response['items'][0]
    found = False

    for x in response['items']:
        #print(x['id']['kind'])
        if x['id']['kind'] == "youtube#video":
            #print("FOUND")
            found = True
            result = x
            #print(result)
            break
    
    if found:
        title = result["snippet"]["title"]
        channel = result["snippet"]["channelTitle"]
        ytlink = "https://www.youtube.com/watch?v=" + result["id"]["videoId"]

        return(title + " : " + ytlink + "\n" + "Uploaded by " + channel)
    else:
        return("No videos found.")

print(ytSearch("black kray 4 bags"))