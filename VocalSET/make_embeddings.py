import openl3
import os
from pydub import AudioSegment


initial_path = "D:\VocalSET\cut_test"
initial_path_out = "D:\VocalSET\embedded_test"

model = openl3.models.load_audio_embedding_model(input_repr="mel256", content_type="music",
                                                 embedding_size=512)

for gender in os.listdir(initial_path):
    for el in os.listdir(initial_path + "\\" + gender):
        for x in os.listdir(initial_path + "\\" + gender + "\\" + el):
            amount_all = len(os.listdir(initial_path + "\\" + gender + "\\" + el + "\\" + x))
            curr_counter = 0
            for audio in os.listdir(initial_path + "\\" + gender + "\\" + el + "\\" + x):
                processed_song = AudioSegment.from_wav(initial_path + "\\" + gender + "\\" + el + "\\" + x + "\\" + audio)
                openl3.process_audio_file(
                        initial_path + "\\" + gender + "\\" + el + "\\" + x + "\\" + audio,
                        output_dir=initial_path_out + "\\" + gender + "\\" + el + "\\" + x,
                        hop_size=0.1,
                        embedding_size=512,
                        input_repr="mel256",
                        model=model)

                curr_counter += 1
                print(f"progress: {curr_counter}/{amount_all}")