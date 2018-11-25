import turtle
import random

answer = raw_input("ti piacerebbe uno scermo pieno di stelle ? ")

while answer.startswith('s') or answer.startswith('S'):
    colors = ["green","blue","orange","red","white","yellow","pink","purple"]
    t = turtle.Pen()
    turtle.bgcolor("black")
    t.reset()
    t.speed(1000)
    for i  in range(10000):
        
        x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
        y = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
        
        size = random.randint(20, 75)
        print i+1, " --> ", size
        color = random.choice(colors)
        t.penup()
        t.setpos(x, y)
        t.left(random.randint(0, 360))
        
        t.color(color)
        
        t.begin_fill()
        t.pendown()
        for j in range(5):
            t.forward(size)
            t.left(220)
            t.forward(size)
            t.left(68)
            
        t.end_fill()
        
    print("E' pieno di stelle")       
    
    answer = raw_input("ti piacerebbe uno scermo pieno di stelle ? ")
    