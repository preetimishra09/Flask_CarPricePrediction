# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:20:54 2023

@author: nilay
"""

from flask import  Flask, render_template,request
import numpy as np
import pickle

app=Flask(__name__)

#route

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict_price():
    kms=float(request.form['km'])
    age=float(request.form['age'])
    oprice=float(request.form['op'])
    fuel=request.form['fuel_type']
    
    if fuel=='Petrol':
       fuel=list([0.0,1.0])  
    elif fuel=='Diesel':
       fuel=list([1.0,0.0])
    else :
       fuel=list([0.0,0.0])

   
    transmission=request.form['transmission']
    if transmission=='Automatic':
       transmission=0.0
    else:
       transmission=1.0
   
    
    data=[np.array([kms,oprice,age,fuel[0],fuel[1],transmission])]
    model = pickle.load(open('./models/lr_model.pkl', 'rb'))
    result=np.round(model.predict(data))    
    msg="Predicted car price is Rs. "+str(result[0])
    return render_template('index.html',prediction_value=msg)



if __name__=="__main__":
    app.run(debug=False)
    


    