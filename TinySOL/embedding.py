import openl3
import os


initial_path = "D:\TinySOL\TinySOL5s"
initial_path_out = "D:\TinySOL\embedded5s"
for category in os.listdir(initial_path):
    for instrument in os.listdir(initial_path+"\\"+category):
        amount_all = len(os.listdir(initial_path+"\\"+category+"\\"+instrument+"\ordinario"))
        curr_counter = 0
        for file in os.listdir(initial_path+"\\"+category+"\\"+instrument+"\ordinario"):
            openl3.process_audio_file(initial_path+"\\"+category+"\\"+instrument+"\ordinario"+"\\" + file,
                                      output_dir=initial_path_out+"\\"+category+"\\"+instrument+"\ordinario",
                                      hop_size=0.1,
                                      embedding_size=512,
                                      input_repr="mel256")

            curr_counter += 1
            print(f"progress: {curr_counter}/{amount_all}")


