import  turtle
t = turtle.Pen()
colors = ["red","green","yellow","blue"]
for x in range(1000):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(45)