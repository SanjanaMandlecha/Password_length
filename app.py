from flask import Flask,request,render_template,url_for,logging
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# import bcrypt
# import click

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Task_1/database.db'
# app.config['SECRET_KEY'] = 'thisissecuritykey'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     User = db.Column(db.String(20), nullable=False, unique=True)
#     Password = db.Column(db.String(80), nullable=False)

#     def __init__(self,user,Password):
#         self.user = user
#         self.password = bcrypt.hashpw(Password.encode('utf-8'),bcrypt.gensalt()).decode()

#     def check_password(self,Password):
#         return bcrypt.checkpw(Password.encode('utf-8'),self.Password.encode('utf-8'))

# with app.app_context():
#     db.create_all()

# @app.route("/")
# def home():
#     return render_template('home.html')

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
      
        # if user == 'Player' and password == 'L@k5hy@(1F':
        if user == 'Player' and password == 'l@k5hy@(tf':
            
            return render_template('/flag.html')

        else:
            return render_template('login.html',error = 'Invalid')
    return render_template('login.html')


@app.route("/flag")
def flag():
    return render_template('flag.html')

@app.route("/asdfghjkl")
def asdfghjkl():
    return render_template('asdfghjkl.html')

if __name__ == '__main__':
    app.run(debug=True)
