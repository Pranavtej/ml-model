from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    one = int(request.form.get('one'))
    two = int(request.form.get('two'))
    three = int(request.form.get('three'))
    four = int(request.form.get('four'))
    five = int(request.form.get('five'))
    six= int(request.form.get('six'))

    # prediction
    result = model.predict(np.array([one , two,three , four ,five , six]).reshape(1,6))

    if result[0] == 1:
        result = 'VERY GOOD'
    elif result[0] == 2:
        result = 'AVERAGE'
    elif result[0] == 3:
        result = 'BELOW AVERAGE'
    elif result[0] == 4:
        result = 'FAIL'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)