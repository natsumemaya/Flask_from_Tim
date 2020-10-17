# static assets or static files (JavaScript, CSS, images). In flask kind of weird way of displaing images in loading in your own custom CSS classes and using your own custom JS. The next video we're gonna talk about blueprints which is what allowes make our flask app into multiple Python files and kind of split it up and make it more organized
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home") #we can have access by both routs
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
