import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle,os
import sys

sys.path.append('../1.Development/')

os.chdir('../1.Development/')
from config import modeloutput_5_features

sys.path.append('../2.Deployment/common_util/')
os.chdir('../2.Deployment/common_util/')
from utility import exceptions
from features import process

os.chdir('../')

# Create flask app
flask_app = Flask(__name__,template_folder='templates')
model = pickle.load(open(modeloutput_5_features, "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [x for x in request.form.values()]
    float_features = list(filter(None, float_features))
    rawinput = [np.array(float_features)]
    input_feats = [x for x in request.form.keys()]
    input_data = dict(zip(input_feats,float_features))
    
    #Exception Handling from utility.py
    check_list = exceptions(input_data)
    #Feature Enginnering from feature.py
    exceptions_list = [u for u,v in check_list.items() if not v]
    
    if len(exceptions_list) == 0:
        input_data_after_feat_eng = process(input_data)
        float_features = [float(v) for u,v in input_data_after_feat_eng.items()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))
    else:
        return render_template("index.html", prediction_text = "Incorrect {}".format([k for k, v in check_list.items() if not v]))
if __name__ == "__main__":
    flask_app.run(debug=True, use_reloader=False)