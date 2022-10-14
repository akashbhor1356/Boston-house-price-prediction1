import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
<<<<<<< HEAD

regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar = pickle.load(open('scaling.pkl','rb'))


=======
## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
>>>>>>> dbe03e71bed14bd5083b6700c0d2be11b5882d00
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
<<<<<<< HEAD
    new_data= scalar.transform(np.array(list(data.values())).reshape(1,-1))
=======
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
>>>>>>> dbe03e71bed14bd5083b6700c0d2be11b5882d00
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
<<<<<<< HEAD
    return render_template("home.html", prediction_text="the house price prediction is {}".format(output))
=======
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

>>>>>>> dbe03e71bed14bd5083b6700c0d2be11b5882d00


if __name__=="__main__":
    app.run(debug=True)
<<<<<<< HEAD

if __name__=='__main__':
    app.run(debug=True)
=======
   
     
>>>>>>> dbe03e71bed14bd5083b6700c0d2be11b5882d00
