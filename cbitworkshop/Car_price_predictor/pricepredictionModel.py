import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as  plt

import pickle

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


with open("pricePredictorModel.pkl",'wb') as f:
    pickle.dump(pipe, f)



# if __name__=="__main__":

#     s = pd.DataFrame({'name': ['Hyundai Santro Xing'], 'company': ['Hyundai'], 'year': [2007], 'kms_driven': [45000], 'fuel_type': ['Petrol']})
#     arr = np.array(['Hyundai Santro Xing', 'Hyundai', 2007, 80000, 45000, 'Petrol'])
#     y_pred = pipe.predict(s)

#     y_test = y_test.reset_index(drop=True)
#     print((y_pred))




