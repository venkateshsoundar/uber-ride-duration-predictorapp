import numpy as np

from flask import Flask, request, render_template
import math
import pickle

app = Flask(__name__)


model2= pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1, -1)
    prediction = model2.predict(final_features)
    output = prediction[0].round(2)
    return render_template('index.html', predict_text="Number of Weekly Riders is: ${}".format(math.floor(output)))
  
if __name__ == "__main__":
    app.run(debug=True)