from flask import Flask, request, url_for, redirect, render_template, jsonify
from joblib import dump, load
# import pandas as pd
# import pickle
# import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)


    prediction = int(prediction.Label[0])
    prediction = clf.predict(query)

    return jsonify({'prediction': list(prediction)})
    # return render_template('home.html',pred='New cases will be{}'.format(prediction))

if __name__ == '__main__':
    rf = joblib.load('rf_model.joblib')
    app.run(debug=True)