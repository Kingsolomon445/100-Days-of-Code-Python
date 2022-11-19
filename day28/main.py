# This is a timer program that sets a number of minutes assigned to complete a task and then some minutes for break
# It does this in a sequence and keep track of your progress by check marking when a work session is completed


from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # To get the current timer event(work or breaks)
timer = None
marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global marks
    global reps

    window.after_cancel(timer)  # Cancels the timer
    canvas.itemconfig(timer_text, text="00:00")
    marks = ""
    reps = 0
    check_mark.config(text=marks)
    label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    global marks

    count_min = int(count // 60)
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # When one session has been completed, move to next session
        start_timer()
        # below is used to check marks when work session completed
        if reps % 2 == 0:
            marks += "✅"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # First step in creating an image for our canvas
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label()
label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(row=0, column=1)

check_mark = Label()
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

start_button = Button(highlightthickness=0, command=start_timer)
start_button.config(text="Start")
start_button.grid(row=2, column=0)

reset_button = Button(highlightthickness=0, command=reset_timer)
reset_button.config(text="Reset")
reset_button.grid(row=2, column=2)

window.mainloop()
