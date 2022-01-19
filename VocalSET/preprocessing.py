from pydub.silence import split_on_silence
from pydub import AudioSegment
import librosa
from pydub.playback import play
import numpy as np
import soundfile as sf
from sklearn.model_selection import train_test_split
import os
from shutil import copyfile
import pandas as pd


def normalize(mode: str):
    pth_train_in = "D:\VocalSET\\train"
    pth_train_out = "D:\VocalSET\\norm_train"
    pth_test_in = "D:\VocalSET\\test"
    pth_test_out = "D:\VocalSET\\norm_test"
    if mode == "train":
        for gender in os.listdir(pth_train_in):
            for el in os.listdir(pth_train_in+  "\\" + gender):
                for x in os.listdir(pth_train_in + "\\" + gender + "\\" + el):
                    for file in os.listdir(pth_train_in + "\\" + gender + "\\" + el + "\\" + x):
                        print("processing "+pth_train_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        y, sr = librosa.load(pth_train_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        std = np.std(y)
                        avg = np.average(y)
                        sf.write(pth_train_out + "\\" + gender + "\\" + el + "\\" + x + "\\" + file, (y - avg) / std, sr, format="wav")
                        print("processed")
    elif mode == "test":
        for gender in os.listdir(pth_test_in):
            for el in os.listdir(pth_test_in+  "\\" + gender):
                for x in os.listdir(pth_test_in + "\\" + gender + "\\" + el):
                    for file in os.listdir(pth_test_in + "\\" + gender + "\\" + el + "\\" + x):
                        print("processing "+pth_test_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        y, sr = librosa.load(pth_test_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        std = np.std(y)
                        avg = np.average(y)
                        sf.write(pth_test_out + "\\" + gender + "\\" + el + "\\" + x + "\\" + file, (y - avg) / std, sr, format="wav")
                        print("processed")


def remove_silence(path: str):
    three_sec_segment = AudioSegment.silent(duration=3000)
    audio = AudioSegment.from_wav(path)
    chunks = split_on_silence(audio, min_silence_len=200, silence_thresh=-16, keep_silence=100)
    for counter, el in enumerate(chunks):
        chunks[counter] = (el + three_sec_segment)[:3001]
        #chunks[counter].export("D:\VocalSET\\tmp\chunk" + str(counter) + ".wav", format="wav")
    return chunks


def cut(mode: str):
    pth_train_in = "D:\VocalSET\\norm_train"
    pth_train_out = "D:\VocalSET\\cut_train"
    pth_test_in = "D:\VocalSET\\norm_test"
    pth_test_out = "D:\VocalSET\\cut_test"
    if mode == "train":
        for gender in os.listdir(pth_train_in):
            for el in os.listdir(pth_train_in + "\\" + gender):
                for x in os.listdir(pth_train_in + "\\" + gender + "\\" + el):
                    for file in os.listdir(pth_train_in + "\\" + gender + "\\" + el + "\\" + x):
                        print("processing " + pth_train_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        chunks = remove_silence(pth_train_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        for counter, chunk in enumerate(chunks):
                            chunk.export(
                                pth_train_out + "\\" + gender + "\\" + el + "\\" + x + "\\" + "c" + str(counter) + file,
                                format="wav")
                        print("processed")
    elif mode == "test":
        for gender in os.listdir(pth_test_in):
            for el in os.listdir(pth_test_in+  "\\" + gender):
                for x in os.listdir(pth_test_in + "\\" + gender + "\\" + el):
                    for file in os.listdir(pth_test_in + "\\" + gender + "\\" + el + "\\" + x):
                        print("processing "+pth_test_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        chunks = remove_silence(pth_test_in + "\\" + gender + "\\" + el + "\\" + x + "\\" + file)
                        for counter, chunk in enumerate(chunks):
                            chunk.export(pth_test_out + "\\" + gender + "\\" + el + "\\" + x + "\\" + "c"+str(counter)+file, format="wav")
                        print("processed")



def split_data():
    filepaths = []
    for gender in os.listdir("D:\VocalSET\FULL"):
        for el in os.listdir("D:\VocalSET\FULL\\" + gender):
            for x in os.listdir("D:\VocalSET\FULL\\" + gender + "\\" + el):
                for file in os.listdir("D:\VocalSET\FULL\\" + gender + "\\" + el +"\\"+x):
                    filepaths.append(gender + "\\" + el +"\\"+x+"\\" + file)
    filepaths = np.array(filepaths).reshape(-1, 1)
    X_train, X_test = train_test_split(filepaths, test_size=0.2)
    X_train, X_test = X_train.flatten(), X_test.flatten()
    for file_train in X_train:
        copyfile("D:\VocalSET\FULL\\" + file_train, "D:\VocalSET\\train\\" + file_train)
    for file_test in X_test:
        copyfile("D:\VocalSET\FULL\\" + file_test, "D:\VocalSET\\test\\" + file_test)


if __name__=="__main__":
    #normalize("test")
    cut("train")

