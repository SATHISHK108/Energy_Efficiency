from flask import Flask, render_template,request
import pickle
import numpy as np

filename = 'energy_efficiency_rfr_model.pkl'
regressor = pickle.load(open(filename,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        comp = float(request.form['Relative Compactness'])
        surf = float(request.form['Surface Area'])
        wall = float(request.form['Wall Area'])
        roof = float(request.form['Roof Area'])
        height = float(request.form['Overall Height'])
        orien = int(request.form['Orientation'])
        glazing = float(request.form['Glazing Area'])
        gla_are = int(request.form['Glazing Area Distribution'])
        
        
        data = np.array([[comp, surf, wall, roof, height, orien, glazing, gla_are]])
        my_prediction = regressor.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
    
if __name__ == '__main__':
        app.run(debug=True,use_reloader=False)