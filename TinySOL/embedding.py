import openl3
import os
from pydub import AudioSegment


def calculate_hop(duration):
    return duration/30


initial_path = "D:\TinySOL\TinySOL"
initial_path_out = "D:\TinySOL\embedded"
for category in os.listdir(initial_path):
    for instrument in os.listdir(initial_path+"\\"+category):
        amount_all = len(initial_path+"\\"+category+"\\"+instrument+"\ordinario")
        curr_counter = 0
        for file in os.listdir(initial_path+"\\"+category+"\\"+instrument+"\ordinario"):
            processed_song = AudioSegment.from_wav(initial_path+"\\"+category+"\\"+instrument+"\ordinario"+"\\" + file)
            openl3.process_audio_file(initial_path+"\\"+category+"\\"+instrument+"\ordinario"+"\\" + file,
                                      output_dir=initial_path_out+"\\"+category+"\\"+instrument+"\ordinario",
                                      hop_size=calculate_hop(processed_song.duration_seconds),
                                      embedding_size=512,
                                      input_repr="mel256")

            curr_counter += 1
            print(f"progress: {curr_counter}/{amount_all}")


