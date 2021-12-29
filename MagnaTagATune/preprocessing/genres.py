import pandas as pd

instruments = ['classical', 'techno', 'electronic', 'rock', 'indian', 'opera', 'pop', 'classic', 'new age', 'dance'
               , 'country', 'metal']
mood = ['slow', 'fast', 'ambient', 'loud', 'quiet', 'soft', 'weird']
y = pd.read_csv("D:\MagnaTagATune\\top_labels.csv", index_col=0)
y = y[mood]
print((y.sum(axis=0)).sum())
y_rep = pd.DataFrame(data=y.sum(axis=0), columns=["True_amount"])
y_rep['True_percent'] = y_rep['True_amount'].apply(lambda x: x/25680*100)
print(y_rep)

y_instr = pd.read_csv("D:\MagnaTagATune\\top_labels.csv", index_col=0)[instruments]
y_rep_instr = pd.DataFrame(data=y_instr.sum(axis=0), columns=["True_amount"])
y_rep_instr['True_percent'] = y_rep_instr['True_amount'].apply(lambda x: x/25680*100)
print(y_rep_instr)