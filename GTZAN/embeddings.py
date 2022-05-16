import numpy as np
import openl3
import os
import librosa
import pandas as pd
import csv


def embedding_mfcc(path_in: str, path_out_csv: str):
    x = []
    labels = []
    for directory in os.listdir(path_in):
        for file in os.listdir(path_in + '/' + directory):
            src, sr = librosa.load(path_in + '/' + directory + '/' + file)
            mfcc = librosa.feature.mfcc(y=src, sr=sr, n_mfcc=20)
            dmfcc = mfcc[:, 1:] - mfcc[:, :-1]
            ddmfcc = dmfcc[:, 1:] - dmfcc[:, :-1]
            x.append(np.concatenate((np.mean(mfcc, axis=1), np.std(mfcc, axis=1),
                                     np.mean(dmfcc, axis=1), np.std(dmfcc, axis=1),
                                     np.mean(ddmfcc, axis=1), np.std(ddmfcc, axis=1))
                                    , axis=0))
            labels.append(directory)
    x_df = pd.DataFrame(x)
    x_df.to_csv(path_out_csv + "/features_mfcc.csv", index=False, header=False)
    labels_df = pd.DataFrame(labels)
    labels_df.to_csv(path_out_csv+"/labels_mfcc.csv", index=False, header=False)


def embedding_l3(path_in: str, path_out_emb: str, path_out_csv: str):
    for directory in os.listdir(path_in):
        for file in os.listdir(path_in + '/' + directory):
            openl3.process_audio_file(path_in + '/' + directory + '/' + file, output_dir=path_out_emb + '/' + directory, hop_size=0.5,
                                      embedding_size=512)

    x = []
    labels = []
    for directory in os.listdir(path_out_emb):
        for file in os.listdir(path_out_emb + '/' + directory):
            x.append((np.load(path_out_emb + '/' + directory + '/' + file))['embedding'].flatten()[0:30720])
            labels.append(directory)

    with open(path_out_csv + "/features_l3.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerows(x)

    with open(path_out_csv+"/labels.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerows(labels)
