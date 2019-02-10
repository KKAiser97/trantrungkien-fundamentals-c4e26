from turtle import *
speed(10)
colors=['red', 'blue', 'brown', 'yellow', 'grey']
n=len(colors)
for j in range(n):
    begin_fill()
    for i in range (2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    fillcolor(colors[j])
    forward(50)
    end_fill()
mainloop()