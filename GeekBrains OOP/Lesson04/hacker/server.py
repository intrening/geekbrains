from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")


@app.route("/secret_page")
def secret_page():
    if request.args["key"] == "87":
        return "HACHERS"
    else:
        return ("Incorrect key!" + request.args["key"])

if __name__ == "__main__":
    app.run()