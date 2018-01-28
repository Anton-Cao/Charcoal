import numpy as np
import pandas as pd
import _pickle as cPickle

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline

from utils import conv, num_previous

data = pd.read_csv("training_data.csv")

X = data[[f'p{i}' for i in range(1, num_previous + 1)]].values
y = data[['p0']].values.ravel()

enc = OneHotEncoder(sparse=False)

print('training')

model = make_pipeline(enc, LogisticRegression())
model.fit(X, y)

print('done training')

with open('model.pkl', 'wb') as f:
    cPickle.dump(model, f)


