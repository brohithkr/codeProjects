import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as  plt

cars = pd.read_csv("cleaned_car.csv")


X = cars.drop(columns=['Price'])
Y = cars['Price']

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=433)


one = OneHotEncoder()
one.fit(X[['name','company','fuel_type']])

column_trans = make_column_transformer((OneHotEncoder(categories= one.categories_),['name','company','fuel_type']),remainder='passthrough')

lr = LinearRegression()

pipe = make_pipeline(column_trans,lr)

pipe.fit(x_train,y_train)

y_pred = pipe.predict(x_test)

y_test = y_test.reset_index(drop=True)


plt.plot(y_pred,label = "y_pred")
plt.plot(y_test,label = "y_test")


plt.savefig('temp.jpg')
plt.show()

