import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import generate_csrf

from forms import LoginForm


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app


app = create_app()
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    form.csrf_token.data = generate_csrf()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.email.data == "admin@email.com" and form.password.data == "12345678":
                return render_template('success.html')
            else:
                return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
