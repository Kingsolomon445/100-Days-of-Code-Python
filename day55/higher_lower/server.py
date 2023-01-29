from flask import Flask
from random import randrange

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><iframe src="https://giphy.com/embed/kjhkPCFKyGaj6cOSZR" ' \
           'width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a ' \
           'href="https://giphy.com/gifs/kjhkPCFKyGaj6cOSZR">via GIPHY</a></p> '


num = randrange(10)


@app.route('/<int:guess>')
def check_guess(guess):
    if guess < num:
        return '<h1 style="color: purple;">Too low, Try Again</h1><iframe ' \
               'src="https://giphy.com/embed/TgmiJ4AZ3HSiIqpOj6" width="480" height="270" frameBorder="0" ' \
               'class="giphy-embed" allowFullScreen></iframe><p><a ' \
               'href="https://giphy.com/gifs/gsimedia-bruh-thats-low-bro-TgmiJ4AZ3HSiIqpOj6">via GIPHY</a></p> '
    elif guess == num:
        return '<h1 style="color: purple;">Correct! Good guess</h1><iframe ' \
               'src="https://giphy.com/embed/26tknCqiJrBQG6bxC" width="480" height="446" frameBorder="0" ' \
               'class="giphy-embed" allowFullScreen></iframe><p><a ' \
               'href="https://giphy.com/gifs/election2016-election-2016-presidential-debate-26tknCqiJrBQG6bxC">via ' \
               'GIPHY</a></p> '
    else:
        return '<h1 style="color: red;">Cmon, too high! Guess again!</h1><iframe ' \
               'src="https://giphy.com/embed/YNzg8rHljnqyoSeDqV" width="480" height="480" frameBorder="0" ' \
               'class="giphy-embed" allowFullScreen></iframe><p><a ' \
               'href="https://giphy.com/gifs/high-so-too-YNzg8rHljnqyoSeDqV">via GIPHY</a></p> '


if __name__ == '__main__':
    app.run(debug=True)
