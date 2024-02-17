from turtle import Turtle,Screen
import pandas

def check_validity(user_input):
    states = pandas.read_csv("50_states.csv")
    state_list = (list(states.state))
    print(state_list)
    if user_input in state_list:
        x_y_cor = states[states["state"]==user_input]
        x_y_list = [x_y_cor.x.to_list()[0],x_y_cor.y.to_list()[0]]
        return x_y_list
    
        

screen = Screen()

screen.setup(600,600)
screen.addshape("blank_states_img.gif")
game_is_on = True
turtle = Turtle()
turtle.speed(0)
turtle.shape("blank_states_img.gif")

while(game_is_on):
    
    

    user_input = screen.textinput("Guess the State", "Tell me the name of the state:")
    if user_input=="pakaya":
        game_is_on = False
    x_y_cordinates_of_turtle = check_validity(user_input)
    turtle.penup()
    turtle.goto(x_y_cordinates_of_turtle[0],x_y_cordinates_of_turtle[1])
    turtle.write(user_input,align="center", font=("Arial", 12, "normal"))
    
    turtle.goto(0,0)





screen.mainloop()