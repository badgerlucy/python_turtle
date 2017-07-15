from pyturtle import *

def draw() :
    speed('fastest')

    buff = ask('What hour, minute, second?')
    hour, minute, second = [int(s) for s in buff.split(' ')]

    line_color(80,50,50)
    fill_color(80,50,50)
    line_width(3)
    begin_hover()
    turnto(90)
    forward(240)
    turnto(0)
    end_hover()
    begin_fill()
    turnto(0)
    circle(240,'right')
    end_fill()





    line_color(75,0,25)
    fill_color(75,0,25)
    line_width(15)
    begin_hover()
    turnto(270)
    forward(240)
    end_hover()
    turnto(0)
    mark()
    hour1 = hour * 30
    turn(-hour1)
    forward(150)


    line_color(100,100,75)
    fill_color(100,100,75)
    line_width(10)
    begin_hover()
    back()
    end_hover()
    turnto(0)
    mark()
    turn(-(minute * 6))
    forward(200)


    line_color(100,50,50)
    fill_color(100,50,50)
    line_width(2)
    begin_hover()
    back()
    end_hover()
    turnto(0)
    turn(-(second * 6))
    forward(220)



launch(draw)
