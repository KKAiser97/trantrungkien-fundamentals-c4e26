import random
import calc
x=random.randint(0,9)
y=random.randint(0,9)
# choices=[0,1]
# a=random.choice(choices)
# r=x+y
# if c=='0':
#     print(x,"+",y,"=",r+random.randint(-1,1))
# else:
#     print(x,"+",y,"=",r)
#     # string formating
#     # s=f"{x}+{y}={r}"
# answer=input("Choose your answer(t/f):")
# if answer=="t" and c=='1':
#     print("yay")
# elif answer=="f" and c=='0':
#     print("yay")
# elif answer=="t" and c=='0':
#     print("nay")
# elif answer=="f" and c=='1':
#     print("nay")
opr=random.choice(["+","-","*","/"])
error=random.randint(-1,1)
r=calc.evaluate(x,y,opr)+error
s=f"{x}{opr}{y}={r}"
print(s)
answer=input("y/n")
if error==0:
    if answer=="y":
        print("yay")
    else:
        print("nay")
else:
    if answer=="y":
        print("nay")
    else:
        print("yay")



