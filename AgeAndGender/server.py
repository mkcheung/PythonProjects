from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/")
def home():
    return (
       render_template('index.html')
    )

@app.route("/<nameInput>")
def guess_name(nameInput):
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
       render_template('ageAndGender.html', name=nameInput, age=presumedAge, gender=presumedGender)
    )

@app.route("/blog")
def get_blog():
    responseFromNpoint = requests.get('https://api.npoint.io/81f40b5d0091e9b4cb74')
    responseFromNpoint.raise_for_status();
    blogInfo = responseFromNpoint.json();

    return (
       render_template('blog.html', posts=blogInfo)
    )

if __name__ == "__main__":
    app.run(debug=True)
