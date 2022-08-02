from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='static/none.png', href3='')
    else:
        myage = request.form['age']
        mysalary = request.form['salary']
        mycar = ''
        if str(myage) =='' or str(mysalary) =='':
            return render_template('index.html', href2='static/none.png', href3='Please insert your age and salary.')
        else:
            model = load('app/Car-Recommender.joblib')
            np_arr = np.array([myage, mysalary])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            
            if 'CUV' in predictions_to_str:
                mycar = 'static/CUV.png'
            elif 'Micro' in predictions_to_str:
                mycar = 'static/Micro.png'
            elif 'Sedan' in predictions_to_str:
                mycar = 'static/Sedan.png'
            elif 'SUV' in predictions_to_str:
                mycar = 'static/SUV.png'
            else:
                mycar = 'static/none.png' 
                
            return render_template('index.html', href2=str(mycar), href3='This is the recommendation! (age:'+str(myage)+' ,salary:'+str(mysalary)+'):'+predictions_to_str)
        

