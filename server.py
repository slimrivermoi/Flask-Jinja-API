from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/guess/<input_name>")
def name_prediction(input_name):
    name = input_name.title()

    # to obtain gender data https://genderize.io/documentation#basic-usage
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data_gender = response.json()
    gender = data_gender["gender"]

    # to obtain age data https://agify.io/documentation#overview
    response_age = requests.get(url=f"https://api.agify.io?name={name}")
    response_age.raise_for_status()
    data_age = response_age.json()
    age = data_age["age"]

    return render_template("index.html", final_name=name, final_gender=gender, final_age=age)


if __name__ == "__main__":
    app.run(debug=True)
