import tkinter as tk
from tkinter.font import Font

import random
import time


class Application(tk.Frame):
    generated_sentence = ""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Application.generated_sentence = self.generate_words()
        self.instructions = tk.Label(self,
                                     text="How fast are your fingers?\nClick Start and Type the following sentence as fast as you can:")
        self.instructions.pack()

        self.sentence = tk.Label(self, text=Application.generated_sentence, font=Font(size=18), wraplength=500)
        self.sentence.pack()

        self.text = tk.Text(self, font=Font(size=15))
        self.text.pack()

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack()

        self.result = tk.Label(self, text="", font=("Arial", 14), wraplength=500)
        self.result.pack()

    def generate_words(self):
        with open("words.txt") as file:
            sentence = "  ".join([word.strip() for word in random.sample(file.readlines(), 40)])
            print(sentence)
            return sentence

    def start(self):
        self.sentence.config(state='disabled')
        self.text.config(state='normal')
        self.text.focus_set()

        start_time = time.time()
        print(start_time)
        self.text.bind('<KeyRelease>', lambda event: self.check_typing(start_time))

    def check_typing(self, start_time):
        entered_text = self.text.get("1.0", 'end').lower().strip()
        sentence = Application.generated_sentence.lower().strip()
        end_time = time.time()
        print(end_time)
        elapsed_time = end_time - start_time
        print(elapsed_time)

        if elapsed_time >= 60:
            self.text.config(state='disabled')
            wrong_words = self.get_incorrect_words(sentence, entered_text)
            wpm = len(entered_text) / 5 / elapsed_time * 60
            self.result["text"] = f"Time's up!\nYou typed at {wpm:.2f} words per minute.\n" + "Incorrect words: " + ", ".join(wrong_words) + ". "
        elif entered_text == sentence:
            wpm = len(sentence) / 5 / elapsed_time * 60
            self.result["text"] = f"You typed at {wpm:.2f} words per minute."
            self.text.config(state='disabled')
            self.text.delete("1.0", 'end')


    def get_incorrect_words(self, sentence, entered_text):
        entered_words = entered_text.split(" ")
        sentence_words = sentence.split(" ")
        incorrect_words = []
        for i in range(len(sentence_words)):
            try:
                if entered_words[i] != sentence_words[i]:
                    incorrect_words.append(sentence_words[i])
            except IndexError:
                incorrect_words.append(sentence_words[i])

        return incorrect_words


root = tk.Tk()
root.geometry("800x800")
root.title("Typing Speed Test")
app = Application(master=root)
app.mainloop()
