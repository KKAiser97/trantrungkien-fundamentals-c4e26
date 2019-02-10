from turtle import *
speed(999)
colors=['red', 'blue', 'brown', 'yellow', 'grey']
n=len(colors)
m=3
for i in range(n):
    for i in range (m):
        pencolor(colors[m-3])
        forward(200)
        left(180-(1-2/m)*180)
    m+=1
mainloop()