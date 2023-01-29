from tkinter import *
from tkinter import messagebox
from random import randint, choice, sample
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    password += ''.join(choice(letters) for _ in range(randint(8, 10)))
    password += ''.join(choice(numbers) for _ in range(randint(2, 4)))
    password += ''.join(choice(symbols) for _ in range(randint(2, 4)))

    password = ''.join(sample(password, len(password)))
    entry3.insert(0, password)
    pyperclip.copy(password)  # copies password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    new_data = {
        entry1.get(): {
            "email": entry2.get(),
            "password": entry3.get(),
        }
    }
    if len(entry1.get()) < 1 or len(entry3.get()) < 1:
        messagebox.showinfo(title="Invalid", message="The fields can't be empty!")
    else:
        is_ok = messagebox.askokcancel(title=entry1.get(), message=f"These are the details entered:  \nEmail: "
                                                                   f"{entry2.get()} \nPassword: {entry3.get()}"
                                                                   f"\nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    updated_data = json.load(data)  # reading data from json
                    updated_data.update(new_data)  # updating the json file with new data
            except FileNotFoundError:
                updated_data = new_data
            finally:
                with open("data.json", "w") as data:
                    json.dump(updated_data, data, indent=4)  # updating json if exists else writing to json
        entry1.delete(0, END)  # Deletes between two indices provided simply first, end
        entry3.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("data.json") as data:
            data = json.load(data)
            try:
                messagebox.showinfo(title=entry1.get(), message=f"Email: {data[entry1.get()]['email']}\n"
                                                                f"Password: {data[entry1.get()]['password']}")
            except KeyError:
                messagebox.showinfo(title="Not Found", message="Password Not Found!")
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="File Not Found!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)

entry1 = Entry(width=20)
entry1.focus()  # This makes the cursor to type focused on this entry at every usage
entry1.grid(row=1, column=1)

entry2 = Entry(width=37)
entry2.insert(0, "")  # This allows the entry to always have a starting email
entry2.grid(row=2, column=1, columnspan=2)

entry3 = Entry(width=20)
entry3.grid(row=3, column=1)

button = Button(text="Add", width=36, command=save_password)
button.grid(row=4, column=1, columnspan=2)

button1 = Button(text="Search", width=13, command=search_password)
button1.grid(row=1, column=2)

button3 = Button(text="Generate Password", command=generate_password)
button3.grid(row=3, column=2)

window.mainloop()
