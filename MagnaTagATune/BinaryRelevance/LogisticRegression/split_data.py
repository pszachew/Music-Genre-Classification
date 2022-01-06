import pandas as pd
from sklearn.model_selection import train_test_split


mood = ['slow', 'fast', 'ambient', 'loud', 'quiet', 'soft', 'weird']

X = pd.read_csv("D:\MagnaTagATune\MagnaTagATune_emb.csv", header=None)
y = pd.read_csv("D:\MagnaTagATune\\top_labels.csv")[mood]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

X_test.to_csv("D:\MagnaTagATune\MagnaTagATune_emb_test.csv", index=False, header=None)
y_test.to_csv("D:\MagnaTagATune\\top_labels_test.csv", index=False)
