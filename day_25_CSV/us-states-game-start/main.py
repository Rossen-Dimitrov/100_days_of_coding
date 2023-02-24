import turtle
import pandas
from write_answer import CorrectAnswer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write_state = CorrectAnswer

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess state").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]

        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        write_state(int(state_data.x), int(state_data.y), answer_state)


