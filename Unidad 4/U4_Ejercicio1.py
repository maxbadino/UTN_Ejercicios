import turtle as t

t.color('green')
t.shape('turtle')

def adelantar(a):
    t.forward(a)

def rotar(a):
    t.left(a)

rotar(180)
adelantar(200)

for i in range(7):
    rotar(-135)
    adelantar(200)

