from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello' #обязательное условие чтобы работала сессия
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True    #работало и без этого
        name = request.form['nm']
        session['user'] = name
        flash("Login succesful!")
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash("Already logged in!")
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user')
def user():
    if "user" in session: 
        user = session['user']
        #return f'<h1>{user}</h1>'
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if "user" in session: 
        user = session['user']
        flash(f'You have been logged out, {user}!', "info") #info as a cathegory if wants t show some icons and stuff bihind you can use the cathegory to do that
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)