import pandas as pd
from sklearn.model_selection import train_test_split

X = pd.read_csv("D:\MagnaTagATune\MagnaTagATune_emb_test.csv", header=None)
y = pd.read_csv("D:\MagnaTagATune\\top_labels_test.csv")

Xa, Xb, ya, yb = train_test_split(X, y, random_state=10, test_size=0.5)

X1, X2, y1, y2 = train_test_split(Xa, ya, random_state=10, test_size=0.5)

X3, X4, y3, y4 = train_test_split(Xb, yb, random_state=10, test_size=0.5)

X1.to_csv("D:\MagnaTagATune\\testcsv\Xtest1.csv", index=False, header=None)
y1.to_csv("D:\MagnaTagATune\\testcsv\ytest1.csv", index=False)

X2.to_csv("D:\MagnaTagATune\\testcsv\Xtest2.csv", index=False, header=None)
y2.to_csv("D:\MagnaTagATune\\testcsv\ytest2.csv", index=False)

X3.to_csv("D:\MagnaTagATune\\testcsv\Xtest3.csv", index=False, header=None)
y3.to_csv("D:\MagnaTagATune\\testcsv\ytest3.csv", index=False)

X4.to_csv("D:\MagnaTagATune\\testcsv\Xtest4.csv", index=False, header=None)
y4.to_csv("D:\MagnaTagATune\\testcsv\ytest4.csv", index=False)

