import urllib.request
import re
import youtube_dl
import os
from pytube import YouTube


urls=[]
hello=[]

search_keyword="add search keywords(no space)"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

print(video_ids)
for i in range(len(video_ids)):
    urls.append("https://www.youtube.com/watch?v=" + video_ids[i])

for i in urls:
    video = YouTube(i)  
    age_res=video.age_restricted
    if age_res==True:
        urls.remove(i)
print(len(urls))
urls=list(set(urls))
print(len(urls))
print("\n total number of videos available for download = "+ str(len(urls)))
b=int(input("\n enter the starting range for download = "))
c=int(input("\n enter the end range for download = "))

path_output='add output path here '

ydl_opts = {}
os.chdir(path_output)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    z=b
    for i in range(b,c):
        
        print(z)
        ydl.download([urls[z]])
        z=z+1
