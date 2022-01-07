import tensorflow as tf
import openl3
import os

directory = ['speech', 'music']

path_in = "D:\GTZAN_speech_music\music_speech\wav"
path_out = "D:\GTZAN_speech_music\music_speech\embedded"

for direct in directory:
    amount_all = len(os.listdir(path_in + "\\" + direct))
    curr_counter = 0
    for file in os.listdir(path_in + "\\" + direct):
        openl3.process_audio_file(path_in + '\\' + direct + '\\' + file, output_dir=path_out + '\\' + direct,
                                  hop_size=1, embedding_size=512)

        curr_counter += 1
        print(f"progress: {curr_counter}/{amount_all}")
