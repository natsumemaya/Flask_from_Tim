# adding Bootstrap and Template inheritance 'POST' & 'GET' methods
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    #return "Hello my first page"
    return render_template('base.html')

@app.route('/child')
def child():
    return render_template('child.html')

@app.route('/usr')
def user(usr):
    if "user" in session: 
        return f'<h1>{usr}</h1>'
    else:
        flash("You're not logged in!")  
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        if request.form['nm']:
            name = request.form['nm']
            session['user'] = name
            flash("Login succesfull!")
            return redirect(url_for('user', usr=name))
        return render_template('login.html')
    else:
        if 'user' in session:
            name = session['user']
            flash("You've already logged in!")
            return redirect(url_for('user', usr=name))
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)

