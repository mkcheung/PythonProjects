from flask import Flask, render_template
import json
import requests


app = Flask(__name__)

@app.route('/')
def home():
    responseFromNpoint = requests.get('https://api.npoint.io/81f40b5d0091e9b4cb74')
    responseFromNpoint.raise_for_status();
    blogInfo = responseFromNpoint.json();
    return render_template("index.html", posts=blogInfo)


@app.route('/show_post/<int:id>')
def show_post(id):
    responseFromNpoint = requests.get('https://api.npoint.io/81f40b5d0091e9b4cb74')
    responseFromNpoint.raise_for_status();
    blogInfo = responseFromNpoint.json();
    selectedPost = [post for post in blogInfo if post['id'] == id ]
    print(selectedPost)
    return render_template("post.html", title=selectedPost[0]['title'], subtitle=selectedPost[0]['subtitle'], body=selectedPost[0]['body'] )

if __name__ == "__main__":
    app.run(debug=True)
