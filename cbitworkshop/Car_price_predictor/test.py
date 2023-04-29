import pickle
import numpy as np
import pandas as pd
with open('pricePredictorModel.pkl','rb') as f:
    model = pickle.load(f)

# print(model)

s = pd.DataFrame({'name': ['Hyundai Santro Xing'], 'company': ['Hyundai'], 'year': [2007], 'kms_driven': [45000], 'fuel_type': ['Petrol']})



predicted = model.predict(s)

print(predicted)