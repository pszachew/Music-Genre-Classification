from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from skmultilearn.problem_transform import BinaryRelevance
import joblib
from sklearn.metrics import accuracy_score

mood = ['slow', 'fast', 'ambient', 'loud', 'quiet', 'soft', 'weird']

X = pd.read_csv("D:\MagnaTagATune\MagnaTagATune_emb.csv", header=None)
y = pd.read_csv("D:\MagnaTagATune\\top_labels.csv")[mood]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)
model = BinaryRelevance(LogisticRegression(max_iter=10000))
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print(accuracy_score(y_test, predicted))
filename = 'log_reg_model_mood.sav'
joblib.dump(model, filename)
