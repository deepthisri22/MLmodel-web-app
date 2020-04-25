import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

IRIS_FOLDER = os.path.join('static', 'class_images')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IRIS_FOLDER

model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    imagename = output + ".jpg"
    print(output)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], imagename)

    return render_template('prediction.html', prediction_text='Predicted Class: {}'.format(output), user_image = full_filename)


@app.route('/returntohome',methods=['POST'])
def returntohome():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)