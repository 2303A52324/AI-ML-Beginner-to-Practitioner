from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    study=float(request.form["study"])
    attendance=float(request.form["attendance"])
    previous=float(request.form["previous"])

    values=np.array([[study,attendance,previous]])

    values=scaler.transform(values)

    prediction=model.predict(values)[0]

    return render_template(
        "index.html",
        prediction=round(prediction,2)
    )

if __name__=="__main__":
    app.run(debug=True)