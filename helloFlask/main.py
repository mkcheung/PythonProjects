from flask import Flask

app = Flask(__name__)
print(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def bold(function):
    def addBold():
        contentToBeWrappedInBold = function()
        return f"<b>{contentToBeWrappedInBold}</b>"
    return addBold

def emphasis(function):
    def addEmphasis():
        contentToEmphasize = function()
        return f"<em>{contentToEmphasize}</em>"
    return addEmphasis

def underlined(function):
    def addUnderline():
        contentToUnderline = function()
        return f"<u>{contentToUnderline}</u>"
    return addUnderline

@app.route("/bye")
@bold
@emphasis
@underlined
def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)