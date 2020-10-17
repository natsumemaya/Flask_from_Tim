from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

content = ['one','two','three']

@app.route('/')
def home():
    #return "Hello my first page"
    return render_template('index.html', content=content)

@app.route("/<name>")
def any_name(name):
    return f'Hello {name}'

@app.route("/admin")
def admin():
    return redirect(url_for("any_name", name='user'))

