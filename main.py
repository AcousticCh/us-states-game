import turtle
import pandas as pd

# create states class with write state and check if answered methods

screen = turtle.Screen()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title = "U.S. States Game"

states_correct = []
states_correct_count = 0

states_data = pd.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

exit_cmd = "Exit"

answer = screen.textinput(title="Guess The State", prompt="name a state")


while states_correct_count < 50:
    test_ans = answer.title()
    if test_ans == exit_cmd:
        break

    if test_ans in states_list:
        state_data = states_data[states_data.state == test_ans]
        states_printed = turtle.Turtle()
        states_printed.hideturtle()
        states_printed.penup()
        states_printed.setposition(int(state_data.x), int(state_data.y))
        states_printed.write(f"{test_ans}")
        states_correct.append(test_ans)
        states_correct_count += 1
    answer = screen.textinput(title=f"{states_correct_count}/50 Correct", prompt="name another state")

for s in states_correct:
    if s in states_list:
        states_list.remove(s)


states_to_learn = pd.Series(states_list, name="states to study")
states_to_learn.to_csv("./states_to_learn.csv", index=False)
