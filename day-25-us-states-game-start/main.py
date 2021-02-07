import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")

#screen add new shape
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
correct_states = []

def print_state(state_name):
    correct_states.append(state_name)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state_name]
    t.goto(int(state_data.x),int(state_data.y))
    t.write(answer_state)#grab the first item of the data




while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state name?")
    guess = answer_state.title()

    if guess == "Exit":
        break

    if guess in all_states:
        print_state(guess)

#states_to_learn.csv
# states_to_learn = []
# for state in all_states:
#     if state not in correct_states:
#         states_to_learn.append(state)

states_to_learn = [state for state in all_states if state not in correct_states]
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")




def get_mouse_click_coor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# screen.exitonclick()
