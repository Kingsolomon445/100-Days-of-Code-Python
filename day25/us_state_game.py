import turtle as t
import pandas as pd

screen = t.Screen()
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")

answer = screen.textinput("U.S States Game", "Guess A State")

# This reads data from the csv file and create a list of states and positions(x,y) from it
states_data = pd.read_csv("50_states.csv")
states = states_data["state"].to_list()
x_values = states_data["x"].to_list()
y_values = states_data["y"].to_list()
pos = list(zip(x_values, y_values))
states_gotten = []

correct_count = 0

# This is the main game processes...game ends when all 50 states have been guessed correctly.
while correct_count < 50:
    answer = answer.title()
    if answer == "Exit":   # Exit is secret word to end the game
        break
    t_write = t.Turtle()
    t_write.hideturtle()
    t_write.penup()
    if answer in states:
        states_gotten.append(answer)
        idx = states.index(answer)
        t_write.goto(pos[idx])
        t_write.write(answer, align="center", font=('Arial', 8, 'normal'))
        correct_count += 1
    answer = screen.textinput(f"{correct_count} / 50", "Guess Another State")

# This saves a csv file of missed states to learn
states_not_gotten = [state for state in states if state not in states_gotten]
states_not_gotten = {"states you missed": states_not_gotten}
states_not_gotten = pd.DataFrame.from_dict(states_not_gotten)
states_not_gotten.to_csv("missing_states.csv")
