import os
from pytube import YouTube

print("Loading...")

print(
"""__________________________________
| ☭ Coммuиisт уоuтuве Dошиlоаdея ☭|
|                                 |
\_ _ _ _ _ _By PoLocHiK_ _ _ _ _ _/
""")

option = str(input("Do you want to download audio or video: \nType 1, if you want to download audio\nType 2,if you want to download video  "))

if option == "1":
    url = input("Enter the YouTube URL: ")
    try:
        yt = YouTube(url)
        mp3files = yt.streams.filter(only_audio=True).first()
        save_path = input("Enter the path where the file should be downloaded: ")
        try:
            out_file = mp3files.download(save_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("File is downloaded in the given path")
        except:
            print("Error occured!")
    except:
        print("Not a valid YouTube URL")

elif option == "2":
    url = input("Enter the YouTube URL: ")
    try:
        yt = YouTube(url)
        mp4files = yt.streams.get_highest_resolution()
        save_path = input("Enter the path where the file should be downloaded: ")
        mp4files.download(save_path)
        print("File is downloaded in the given path")
    except:
        print("Not a vaild YouTube URL")
