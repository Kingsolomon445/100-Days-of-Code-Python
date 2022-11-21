from tkinter import *
import pandas
from random import choice
from os.path import isfile  # to check if a file exists in path indicated

BACKGROUND_COLOR = "#B1DDC6"
idx = 0

if isfile("data/words_to_learn.csv"):
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
else:
    words_to_learn = pandas.read_csv("data/french_words.csv")
words_to_learn = words_to_learn.to_dict(orient="records")
new_pair = {}
french_word, english_word = None, None
words_learned = []


def on_closing():
    global words_learned, words_to_learn

    words_learned = pandas.DataFrame(words_learned)
    words_learned.to_csv("data/words_learned.csv", mode="a", index=False)
    words_to_learn = pandas.DataFrame(words_to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)

    window.destroy()


def track_progress():  # To keep tracked of learned and unlearned words
    words_learned.append(new_pair)
    words_to_learn.remove(new_pair)


def generate_pair():
    global french_word, english_word, new_pair
    new_pair = choice(words_to_learn)
    french_word, english_word = (value for key, value in new_pair.items())  # Unpacks the values to the variables


def english_card():
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfig(word1, text="English", fill="white")
    canvas.itemconfig(word2, text=english_word, fill="white")


def french_card():
    generate_pair()
    global idx, timer
    window.after_cancel(timer)  # prevents the automatic flipping if user press the right or wrong button abruptly
    canvas.itemconfig(img, image=front_img)
    canvas.itemconfig(word1, text="French", fill="black")
    canvas.itemconfig(word2, text=french_word, fill="black")
    timer = window.after(3000, english_card)  # flips for english card after 3 seconds


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0)

window.protocol("WM_DELETE_WINDOW", on_closing)  # To perform an action when user exits program

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=front_img)
word1 = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word2 = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
# Using lambda to pass multiple commands to the right button
right_button = Button(image=right_img, command=lambda: [track_progress(), french_card()])
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=french_card)
wrong_button.grid(row=1, column=0)

timer = window.after(0, func=french_card)  # To start the flipping

window.mainloop()
