#Blueprints that alloweds us to divide out app into separate Python files we can pass specific views and rendertemplates from different areas of kind of progect (admin page^ or login scrip that you could reuse in different applications)
from flask import Flask, render_template
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin") #/admin/(home,test)

@app.route("/")
def home():
    return '<h1>Test</h1>'

if __name__ == '__main__':
    app.run(debug=True)
