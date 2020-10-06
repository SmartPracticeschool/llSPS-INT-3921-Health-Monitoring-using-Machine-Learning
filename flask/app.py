from flask import Flask, request, render_template
import joblib
app = Flask(__name__)
model =joblib.load("health.sav")

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==0):
        prediction="Everything is fine"
        return render_template("index.html")
    elif(output==1):
        prediction="Needed some Medication"
        return render_template("index.html")
    else:
        prediction="Needed to consult Doctor "
        return render_template('index.html',
        prediction_text=prediction)
if __name__ == "__main__":
    app.run(debug=True)


