import pandas as pd
from shapely.geometry import Point, shape

from flask import Flask
from flask import render_template
import json


data_path = '/Users/Jackie/Desktop/Data Science/Kaggle/'
n_samples = 30000

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    df_clean=pd.read_csv('/Users/Jackie/Desktop/Data Science/Kaggle/dashboard/data.csv')
    return df_clean.to_json(orient='records')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
