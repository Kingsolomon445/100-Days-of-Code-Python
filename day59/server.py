import smtplib

from flask import Flask, render_template, request
import requests
from datetime import datetime

MY_EMAIL = ""
MY_PASSWORD = ""

app = Flask(__name__)


def send_email(data):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, data)


@app.route('/')
def home():
    data = requests.get("https://api.npoint.io/4edef7e034d2c3b6ad6e").json()
    author = "Oluwaseyi"
    date = f"{datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}"
    return render_template('index.html', posts=data, author=author, date=date)


@app.route('/post/<int:id>')
def post(id):
    data = requests.get("https://api.npoint.io/4edef7e034d2c3b6ad6e").json()
    author = "Oluwaseyi"
    date = f"{datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}"
    return render_template('post.html', posts=data, id=id, author=author, date=date)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        for entry in request.form:
            send_email(entry + ": " + request.form[entry])
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
