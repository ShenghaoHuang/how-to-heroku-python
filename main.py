from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/sheng")
def sheng():
    return render_template('sheng.html')

@app.route("/index")
def fancy():
    return render_template(('index.html'))