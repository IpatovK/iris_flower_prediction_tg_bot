from IPython.display import display
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("~/.cache/kagglehub/datasets/arshid/iris-flower-dataset/versions/1/IRIS.csv")
display(data.head())
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']
display(data.isnull().sum())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
log_reg = LogisticRegression(multi_class='multinomial')
log_reg = log_reg.fit(X_train, y_train)
print(log_reg.score(X_test, y_test))
with open('model.pkl','wb') as f:
    pickle.dump(log_reg, f)