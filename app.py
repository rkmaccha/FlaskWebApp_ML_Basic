from flask import Flask, render_template,request
import pickle

app = Flask(__name__)
reg_model = pickle.load(open("lr_multimodel.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/predict", methods = ['POST','GET'])
def predict():
    if request.method =="POST":
        area = request.form['HouseArea']
        bedrooms = request.form['HouseBedrooms']
        age = request.form['HouseAge'] 

        user_data = [[float(area),float(bedrooms),float(age)]]
        
        prediction = reg_model.predict(user_data)
        prediction = round(prediction[0], 2)
        #print(prediction)
        return render_template("index.html", pred = prediction)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)