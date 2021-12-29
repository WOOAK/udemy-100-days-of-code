import turtle
import pandas
import time


screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
print(state_list)
x_list = data["x"].to_list()
y_list = data["y"].to_list()

clock = turtle.Turtle()
clock.penup()
clock.hideturtle()
clock.goto(250, 250)



mark = turtle.Turtle()
mark.hideturtle()
mark.penup()

# get coordinate when click on screen
# def getcoor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(getcoor)
#
# turtle.mainloop()


get = 0

guessed_state = []


while get < 50:
    answer_state = screen.textinput(title = f"{get}/50 States Correct", prompt = "What's another state?").title()


    # def countdown(t):
    #     while t:
    #         mins, secs = divmod(t, 60)
    #         timer = '{:02d}:{:02d}'.format(mins, secs)
    #         # print(timer, end="\r")
    #         clock.clear()
    #         clock.write(timer, font=("Arial", 16, "normal"))
    #         time.sleep(1)
    #         t -= 1
    #
    #     # print('Fire in the hole!!')
    #
    # countdown(300)
# list comprehension day 26
    if answer_state == 'Answer':
        for state in state_list:
            state_data = data[data.state == state]
            mark.goto(int(state_data.x), int(state_data.y))
            mark.write(state, align = "center")
        break
    if answer_state == 'Exit':
        #missing_state = []
        #for state in state_list:
        #    if state not in guessed_state:
        #        missing_state.append(state)
        missing_state = [state for state in state_list if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        #state_pos = state_list.index(answer_state)
        state_data = data[data.state == answer_state]
        mark.goto(int(state_data.x), int(state_data.y))
        #mark.goto(x_list[state_pos], y_list[state_pos])
        mark.write(answer_state, align = "center")
        if answer_state not in guessed_state:
            get += 1
            guessed_state.append(answer_state)
screen.exitonclick()