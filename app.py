from flask import Flask,request,render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("home2.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final = [np.array(float_features)]
    prediction = model.predict(final)


    if prediction == "S":
        return render_template('home2.html', pred="Your Grade will be S 🤩")
    elif prediction == "A+":
        return render_template('home2.html', pred="Your grade will be A+ 😎")
    elif prediction == "A":
        return render_template('home2.html', pred="Your grade will be A 😁")
    elif prediction == "B+":
        return render_template('home2.html', pred="Your grade will be B+ 😄")
    elif prediction == "B":
        return render_template('home2.html', pred="Your grade will be B 😊")
    elif prediction == "C+":
        return render_template('home2.html', pred="Your grade will be C+ ☹️")
    elif prediction == "C":
        return render_template('home2.html', pred="Your grade will be C 😔")
    elif prediction == "D":
        return render_template('home2.html', pred="Your grade will be D 😓")
    elif prediction == "P":
        return render_template('home2.html', pred="Your grade will be P 😖")
    elif prediction == "F":
        return render_template('home2.html', pred="Your grade will be F 😥")
    
if __name__ == '__main__':
    app.run(debug=True)