from turtle import *
speed(9999)
a=20
# for i in range [1,500,10]:
#     forward(i)
#     left(90)
for i in range(500):
    for j in range(2):
        forward(a)
        left(90)
    a = a + 10
mainloop()