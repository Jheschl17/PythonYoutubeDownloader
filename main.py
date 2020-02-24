# to execute run 'python3 main.py <path-to-file-with-links>'
# Downloads videos as mp3 from youtube
# requires ffmpeg to be installed

import sys
import subprocess
from pytube import YouTube

links = []
with open(sys.argv[1]) as file:
    links = map(lambda it: it.strip(), file.readlines())

for link in links:
    print(f"now downloading {link}", end='', flush=True)
    yt = YouTube(link)
    print(" .", end='', flush=True)
    yt.streams.filter(only_audio=True).first().download()
    name = yt.streams.filter(only_audio=True).first().default_filename
    print(" .", end='', flush=True)
    subprocess.run(["ffmpeg", "-i", name, f"{name[:-4]}.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    print(" .", end='', flush=True)
    subprocess.run(["rm", name])
    print(" Done")

