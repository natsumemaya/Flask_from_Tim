# собираемся сохранить юзера создаем новый обьект юзер на странице login
# это довольно странно т.к. обычно создаем аккаунт страницу...
# мы будем просто со страницы user какое бы там ни было написано имя создавать ссылку на аккаунт и не будет никакой безопастности

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy #устанавливаем (pip3 install) и подключаем

app = Flask(__name__)
app.secret_key = 'hello' #обязательное условие чтобы работала сессия
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3' 
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.permanent_session_lifetime = timedelta(minutes=10)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return render_template('base.html')

@app.route("/view")
def view(): #ender template thats is gonna pass in all of the users DB objects
    return render_template('view.html', values=users.query.all())

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True    #работало и без этого
        name = request.form['nm']
        session['user'] = name
        # when user has typed his name need to check if user already exist in our DB
        found_user = users.query.filter_by(name=name).first() #grab information from DB 
        # to delete one! to delete every need to loop it...
        # found_user = users.query.filter_by(name=name).delete() -> commit after!
        # for user in found_user:
        #      user.delete()     
        if found_user: #grab it and store it in a session so then we go to the next page and see that
            session["email"] = found_user.email    
        else: # if hi doesnot exist we create one
            usr = users(name, "") # we're adding him to a database, blink for email because we'll have it on next step
            db.session.add(usr) #добавляем в ДБ (staging area) ждет чтобы действительно добавиться
            db.session.commit() #нужно закомитеть каждый раз когда изменяем данные в ДБ

        flash("Login succesful!")
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash("Already logged in!")
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if "user" in session: 
        user = session['user']
        if request.method == 'POST':
            email = request.form["email"]
            session["email"] = email  
            #when they post their email we need to change it in DB rather than store it in session
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email   
            db.session.commit()
            flash('Email was saived')
        else:
            if 'email' in session:
                email = session["email"]
        return render_template("user.html", email=email, user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if "user" in session: 
        user = session['user']
        flash(f'You have been logged out, {user}!', "info") #info as a cathegory if wants t show some icons and stuff bihind you can use the cathegory to do that
    session.pop("user", None)
    session.pop('email', None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)