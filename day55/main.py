from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/')
def hello_word():
    return 'Hello world!'

@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "bye"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"My name is {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
