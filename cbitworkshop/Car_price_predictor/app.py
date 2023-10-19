from flask import Flask, request, render_template, url_for
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)



@app.route("/", methods=['GET','POST'])
def main():
    price = None
    name = None
    company = None
    year = None
    kms_driven = None
    fuel = None

    data=None

    if request.method == 'POST':
        name = request.form.get('name')
        company = request.form.get('company')
        year = request.form.get('year')
        kms_driven = request.form.get('kms')
        fuel = request.form.get('fuel')
        data = pd.DataFrame({
        'name':[name],
        'company': [company],
        'year': [int(year)],
        'kms_driven': [int(kms_driven)],
        'fuel_type': [fuel]
        })
        print(data)
        with open('pricePredictorModel.pkl','rb') as f:
            model = pickle.load(f)

    
        prices = model.predict(data)
        price=prices[0]

    cars = pd.read_csv('cleaned_car.csv')

    names = np.sort(cars['name'].unique())
    companies = np.sort(cars['company'].unique())
    years = np.sort(cars['year'].unique())
    kms_drivens = np.sort(cars['kms_driven'].unique())
    years = np.sort(cars['year'].unique())
    fuels = (cars['fuel_type'].unique())

    

    return render_template('index.html',companies = companies,names = names,years = years,kms_driven = kms_driven,fuels = fuels,data=data,price=price)




        


if __name__=="__main__":
    app.run(debug=True)