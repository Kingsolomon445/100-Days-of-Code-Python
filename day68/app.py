import os

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    return app


app = create_app()
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# with app.app_context():
#     db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        password = request.form["password"]
        password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        try:
            user = User(
                name=request.form["name"],
                email=request.form["email"],
                password=password,
            )
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(f"{e}")
        return render_template("secrets.html")
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            user = User.query.filter_by(email=request.form["email"]).first()
            if check_password_hash(user.password, request.form["password"]):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Incorrect Password")
        except Exception as e:
            flash(f"This email does not exist!")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory('static',
                               "files/"+filename,
                               as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
