from flask import Flask, request, render_template, url_for
import pandas as pd
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
        data = pd.DataFrame([name,company,year,kms_driven,fuel])

        with open('pricePredictorModel.pkl','rb') as f:
            model = pickle.load(f)

    
        prices = model.predict(data)
        price=prices[0]

    cars = pd.read_csv('cleaned_car.csv')

    names = cars['name'].unique()
    companies = cars['company'].unique()
    years = cars['year'].unique()
    kms_drivens = cars['kms_driven'].unique()
    years = cars['year'].unique()
    fuels = cars['fuel_type'].unique()

    

    return render_template('index.html',companies = companies,names = names,years = years,kms_driven = kms_driven,fuels = fuels,data=data,price=price)




        


if __name__=="__main__":
    app.run(debug=True)