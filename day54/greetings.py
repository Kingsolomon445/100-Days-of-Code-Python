from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello world!'


@app.route('/name')
def say_name():
    return "My name is Oluwaseyi"


if __name__ == "__main__":
    app.run()
