from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/")
def home():
    return '<h1 style="text-align: center;">Enter a /name in the URL to get a gender and age guess.</h1>'

@app.route("/<nameInput>")
def guess(nameInput):
    parameters = {
        "name": nameInput
    }
    responseFromAgeify = requests.get('https://api.agify.io', params=parameters)
    responseFromAgeify.raise_for_status();
    fromAgeify = responseFromAgeify.json();
    presumedAge = fromAgeify['age']

    responseFromGenderize = requests.get('https://api.genderize.io', params=parameters)
    responseFromGenderize.raise_for_status();
    fromGenderize = responseFromGenderize.json();
    presumedGender = fromGenderize['gender']

    return (
       render_template('index.html', name=nameInput, age=presumedAge, gender=presumedGender)
    )

if __name__ == "__main__":
    app.run(debug=True)