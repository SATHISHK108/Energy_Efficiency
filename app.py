{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df90779f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template,request\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "filename = 'energy_efficiency_rfr_model.pkl'\n",
    "regressor = pickle.load(open(filename,'rb'))\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "    if request.method == 'POST':\n",
    "        comp = float(request.form['Relative Compactness'])\n",
    "        surf = float(request.form['Surface Area'])\n",
    "        wall = float(request.form['Wall Area'])\n",
    "        roof = float(request.form['Roof Area'])\n",
    "        height = float(request.form['Overall Height'])\n",
    "        orien = int(request.form['Orientation'])\n",
    "        glazing = float(request.form['Glazing Area'])\n",
    "        gla_are = int(request.form['Glazing Area Distribution'])\n",
    "        \n",
    "        \n",
    "        data = np.array([[comp, surf, wall, roof, height, orien, glazing, gla_are]])\n",
    "        my_prediction = regressor.predict(data)\n",
    "        \n",
    "        return render_template('result.html', prediction=my_prediction)\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "        app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e4d23e4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c690fa34",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
