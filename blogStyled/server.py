from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    responseFromNpoint = requests.get('https://api.npoint.io/deb58d7aa3714b484f3d')
    responseFromNpoint.raise_for_status()
    blogInfo = responseFromNpoint.json()
    return render_template("index.html", blogInfo=blogInfo)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/post/<int:id>')
def show_post(id):
    responseFromNpoint = requests.get('https://api.npoint.io/deb58d7aa3714b484f3d')
    responseFromNpoint.raise_for_status();
    blogInfo = responseFromNpoint.json();
    selectedPost = [ blogData for blogData in blogInfo if blogData['id'] == id]
    return render_template("post.html", title=selectedPost[0]['title'], subtitle=selectedPost[0]['subtitle'], body=selectedPost[0]['body'], image_url=selectedPost[0]['image_url'] )


@app.route('/contact')
def contact():
    return render_template("contact.html")
