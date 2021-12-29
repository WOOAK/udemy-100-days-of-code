import turtle as t
import random as r
is_race_on = False
screen = t.Screen()
screen.setup(500, 500)
colours = ["red", "orange", "yellow", "green", "blue", "purple", "black", "grey"]
number_of_turtle = int(screen.textinput("Start", "How many turtle do you want (Max 8)"))
str = ""
for select in range(number_of_turtle):
    str += f"{colours[select]}/"

user_bet = screen.textinput("Make your bet.", f"Which turtle will win the race? Enter a color({str}):")
amount = int(screen.textinput("Bet amount", "RM"))


turtle_join = []
yy = 230

gap = (yy*2)/(number_of_turtle - 1)

for count in range(number_of_turtle):
    new_turtle = t.Turtle(shape = 'turtle')
    new_turtle.penup()
    new_turtle.color(colours[count])
    new_turtle.goto(x=-230, y = yy)
    turtle_join.append(new_turtle)
    yy -= gap

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtle_join:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
        else:
            step = r.randint(0, 10)
            turtle.forward(step)

if user_bet == winner:
    print(f"You win, the {winner} turtle is the winner. You have win RM{amount*number_of_turtle}")
else:
    print(f"You lose, the {winner} turtle is the winner. You have lost RM{amount}")

screen.exitonclick()
