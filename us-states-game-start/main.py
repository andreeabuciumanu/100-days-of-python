import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
data_list = []
for index in range(0, len(data_dict["state"])):
    new_list = [data_dict["state"][index], data_dict["x"][index], data_dict["y"][index]]
    data_list.append(new_list)

guessed_list = []
missed_states = []

while len(guessed_list) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states =[item[0] for item in data_list if item[0] not in guessed_list]
        missed_states_to_scratch = pandas.DataFrame(missed_states)
        missed_states_to_scratch.to_csv("missed_states.csv")
        break

    for item in data_list:
        if answer_state == str(item[0]):
            guessed_list.append(item[0])
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(item[1]), int(item[2]))
            t.pendown()
            t.write(item[0])

print(missed_states)

