from flask import Blueprint, render_template

second = Blueprint('second', __name__, static_folder='static', template_folder="templates")#define a path to your static folder and template folder

@second.route('/home')
@second.route('/')
def home():
    return render_template("home.html")

@second.route('/test')
def test():
    return '<h1>test</h1>'

#there no neeed to run like we did in main file because we are not gonna running the application from this file we only gonna run it from main
# put this file in its own folder and it has its own static images and its own templates (that means we can take that folder and we can just put that into any flask app and use like a little component)
