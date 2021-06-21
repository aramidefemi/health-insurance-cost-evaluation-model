# web app packages
import requests
from flask import Flask, render_template, redirect, url_for, request,jsonify
from flask_cors import CORS, cross_origin
# from werkzeug.wrappers import Request, Response


# for data loading and transformation
import numpy as np 
import pandas as pd
import json

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import pickle
from app.libs.pricing import get_price
from app.libs.preprocess import prep
from app.libs.estimate import get_plan

model = pickle.load(open("app/models/in_model.pkl", "rb"))
colname = pickle.load(open("app/models/colname.pkl", "rb"))


app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.debug=True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
# @cross_origin()
def predict():
     response = request.json
     type, df = prep(response)
     pred_plan, note = get_plan(type=type, data=df)
     price = get_price(plan=pred_plan)
     return jsonify({'Plan': pred_plan, 'Pricing': price, 'Side note':note})
     


