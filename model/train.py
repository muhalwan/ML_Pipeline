import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv('data/train_data.csv')
X = data.drop('target', axis=1)
y = data['target']

model = LinearRegression().fit(X, y)
joblib.dump(model, 'model/model.pkl')
