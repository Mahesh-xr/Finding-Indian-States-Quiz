import turtle

import pandas
from turtle import Turtle, Screen
# to get hold of number of states

data = pandas.read_csv('indian_states_coordinates.csv')
all_states = data.state.tolist()
writter = Turtle()
writter.hideturtle()
screen = Screen()
screen.setup(800, 800)
screen.title("India-States Quiz")
screen.bgpic("indianmap.png")
guessed_states = []
game_is_on = True
while len(guessed_states)<=28:
        user_answer = screen.textinput(title=f" {len(guessed_states)}/28 states", prompt="What's the another state ?").title()
        if user_answer == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("missing_states.csv")
            break

        if user_answer.title() in all_states:
            guessed_states.append(user_answer)
            current_state = data[data['state'] == user_answer]
            x = current_state['x']
            print(x)
            x = current_state['x'].item()
            print(x)
            y = current_state['y'].item()
            writter.teleport(x, y)
            writter.write(user_answer, False, 'center', ("Courier", 8, "normal"))

# with open("states_to_learn.csv", "w") as learning_file:
#     for state in all_states:
#         if state not in guessed_states:
#             content = data[data.state == state].to_string()
#             learning_file.write(content)
