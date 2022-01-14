import os
from pydub import AudioSegment
import random


def cut_audio(audio: AudioSegment) -> AudioSegment:
    total_in_ms = len(audio)
    end = random.randint(1000, total_in_ms)
    start = end - 1000
    return audio[start:(end+1)]


initial_path = "D:\TinySOL\TinySOL"
initial_path_out = "D:\TinySOL\TinySOL1s"
for category in os.listdir(initial_path):
    for instrument in os.listdir(initial_path+"\\"+category):
        for file in os.listdir(initial_path+"\\"+category+"\\"+instrument+"\ordinario"):
            song = AudioSegment.from_wav(initial_path+"\\"+category+"\\"+instrument+"\ordinario" + "\\"+file)
            final_song = cut_audio(song)
            final_song.export(initial_path_out+"\\"+category+"\\"+instrument+"\ordinario" + "\\"+file, format="wav")

