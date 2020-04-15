import turtle as t

t.shape('turtle')

def adelantar(a):
    t.forward(a)

def rotar(a):
    t.left(a)

for i in range (4):
    t.fillcolor("red")
    t.begin_fill()
    t.pensize(3)
    adelantar(80)
    rotar(225)
    adelantar(80)
    rotar(90)
    t.hideturtle()
    t.end_fill()
    t.fillcolor("green")
    t.begin_fill()
    t.pensize(3)
    adelantar(80)
    rotar(225)
    adelantar(80)
    rotar(90)
    t.hideturtle()
    t.end_fill()






