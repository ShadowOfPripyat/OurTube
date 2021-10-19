import os
from pytube import YouTube

print("Loading...")

print(
"""__________________________________
| ☭ Coммuиisт уоuтuве Dошиlоаdея ☭|
|                                 |
\_ _ _ _ _ _By PoLocHiK_ _ _ _ _ _/
""")

print("Enter the YouTube URL:")
url = input()

print("Working...")
try:
    video= YouTube(url)
    stream = video.streams.get_highest_resolution()
    print("Enter the name of the folder where you want to save the video: ")
    stream.download(output_path = input())
    print("Downloaded succesfully!")
except:
    print("Not a valid YouTube link")
