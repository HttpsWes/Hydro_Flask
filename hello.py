from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "home.html.jinja",
        my_variable="Full cowling!!!",
        list= ["Apple","Banana", "Cookies"]

                            
                            )


@app.route("/ping")
def ping():
    return "<p>pong</p>"

@app.route("/hello/<Wesley>")
def hello(name):
    return f"<p> Hello, {name}! </p>"