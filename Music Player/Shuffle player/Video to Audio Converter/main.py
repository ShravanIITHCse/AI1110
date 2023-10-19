import moviepy.editor
#This module is used to convert video to audio
from tkinter.filedialog import *


vid = askopenfilename()

video = moviepy.editor.VideoFileClip(vid)

aud = video.audio

file_name=input("Specify the name of the file you want to keep after converting to audio : ")

aud.write_audiofile(file_name)

print("---End---")
