# A simple miles to kilometers converter making use of tkinter to produce a GUI

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

label = Label()
label.grid(column=0, row=1)
label.config(text="is equal to")


def miles_to_km():
    km = str(round(float(entry.get()) * 1.609344, 4))
    result_label.config(text=km)


entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.insert(END, string="0")

result_label = Label(text="0")
result_label.grid(column=1, row=1)

label_miles = Label()
label_miles.grid(column=2, row=0)
label_miles.config(text="Miles")

label_km = Label()
label_km.grid(column=2, row=1)
label_km.config(text="Km")

button = Button()
button.grid(column=1, row=2)
button.config(text="Calculate", command=miles_to_km)

mainloop()
