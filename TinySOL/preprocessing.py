import os
from pydub import AudioSegment
initial_path = "D:\TinySOL\TinySOL"
initial_path_out = "D:\TinySOL\TinySOL5"
for category in os.listdir(initial_path):
    for instrument in os.listdir(initial_path+"\\"+category):
        for file in os.listdir(initial_path+"\\"+category+"\\"+instrument+"\ordinario"):
            song = AudioSegment.from_wav(initial_path+"\\"+category+"\\"+instrument+"\ordinario" + "\\"+file)
            final_song = (song+AudioSegment.silent(duration=5000))[0:5000]
            final_song.export(initial_path_out+"\\"+category+"\\"+instrument+"\ordinario" + "\\"+file)