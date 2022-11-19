import os
from pytube import YouTube
from pytube import Playlist

yt_p = int(input("Download YT-Video [1] or YT-Playlist [2]: "))
print()

if yt_p == 1:
    url_vid = input("YT-URL - Video: ")
    yt = YouTube(url_vid)
    
    print(yt.title)
    #print(yt.publish_date)
    #print(yt.length)
    #print(yt.description)
    
    dl_type = int(input("Highest Resolutiuon [1], Lowest Resolution [2], Custom Resolution [3], Just Audio [4]: "))

    if dl_type == 1:
        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)

        yt.streams.get_highest_resolution().download(output_path=path)

    if dl_type == 2:
        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)

        yt.streams.get_lowest_resolution().download(output_path=path)

    if dl_type == 3:
        res = str(input("YT-Video - Resolution [“4320p“, “2160p“, “1440p“, “1080p“, “720p”, “480p”, “360p”, “240p”, “144p”]: "))

        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)

        yt.streams.get_by_resolution(resolution=res).download(output_path=path)
    
    if dl_type == 4:
        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)
        
        yt.streams.get_audio_only().download(output_path=path)

if yt_p == 2:
    print("The Playlist must be public !!!")


    url_pl = input("YT-URL - Playlist: ")
    p = Playlist(url_pl)

    print()
    print(p.title)
    print("Published by",p.owner)
    print(p.length, ("Videos are in the Playlist"))
    print()
    #for i in range(p.length):     

    dl_type = int(input("Highest Resolutiuon [1], Lowest Resolution [2], Custom Resolution [3], Just Audio [4]: "))

    if dl_type == 1:
        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)

        for video in p.videos:
            video.streams.get_highest_resolution().download(output_path=path)
            print("Successfully saved Video.")

    if dl_type == 2:
        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)

        for video in p.videos:
            video.streams.get_lowest_resolution().download(output_path=path)
            print("Successfully saved Video.")

    if dl_type == 3:
        res = str(input("YT-Video - Resolution [“4320p“, “2160p“, “1440p“, “1080p“, “720p”, “480p”, “360p”, “240p”, “144p”]: "))
    
        path = input("Downloadpath [Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print()
        print("Saving in:", path)

        for video in p.videos:
            video.streams.get_by_resolution(res).download(output_path=path)
            print("Successfully saved Video.")
    
    if dl_type == 4:

        path = input("Downloadpath Default “Downloads“]: ")
        if path == "":
            path = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))

        print("Saving in:", path)
    
        for video in p.videos:
            video.streams.get_audio_only().download(output_path=path)
            print("Successfully saved Audio.")