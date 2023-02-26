from flask import Flask, request
from flask_cors import CORS, cross_origin
import joblib
import numpy as np

app = Flask(__name__)
CORS(app) #แก้ปัญหาเรื่อง cross origin ?

@app.route("/")
def hello_word():
    return 'Hello_word'

@app.route("/area",methods=["GET"])
@cross_origin() #ป้องกันปัญหาการติด cross ข้าม domain
def area():
    w = float(request.values["w"])
    h = float(request.values["h"])
    return str(w*h) 
    '''
    #?w=1.5&h=20 เป็นการส่ง parameter ใน url ?-> Get แต่ไม่เป็นที่นิยม ต้องส่งแบบ post
    '''
@app.route('/bmi')
@cross_origin()
def bmi():
    weight = float(request.values["weight"])
    height = float(request.values["height"])
    return str(weight/((height/100)**2))


@app.route("/iris",methods=["POST"])
@cross_origin()
def predict_species():
    model = joblib.load("iris.model")
    req = request.values["param"]
    inputs = np.array(req.split(","),dtype = np.float32).reshape(1,-1)
    predict_target = model.predict(inputs)
    if predict_target == 0:
        return "Setosa"
    elif predict_target == 1:
        return "Versicolor"
    else:
        return "Virginica"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug =True)