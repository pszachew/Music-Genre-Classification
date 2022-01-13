import openl3
import os
from pydub import AudioSegment


def calculate_hop(duration):
    return duration/30


initial_path = "D:\VocalSET\FULL"
initial_path_out = "D:\VocalSET\embedded"

for gender in os.listdir(initial_path):
    if gender not in ["female1"]:
        for el in os.listdir(initial_path + "\\" + gender):
            for x in os.listdir(initial_path + "\\" + gender + "\\" + el):
                amount_all = len(os.listdir(initial_path + "\\" + gender + "\\" + el + "\\" + x))
                curr_counter = 0
                for audio in os.listdir(initial_path + "\\" + gender + "\\" + el + "\\" + x):
                    processed_song = AudioSegment.from_wav(initial_path + "\\" + gender + "\\" + el + "\\" + x + "\\" + audio)
                    openl3.process_audio_file(
                        initial_path + "\\" + gender + "\\" + el + "\\" + x + "\\" + audio,
                        output_dir=initial_path_out + "\\" + gender + "\\" + el + "\\" + x,
                        hop_size=calculate_hop(processed_song.duration_seconds),
                        embedding_size=512,
                        input_repr="mel256")

                    curr_counter += 1
                    print(f"progress: {curr_counter}/{amount_all}")