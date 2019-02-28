from random import *
from calc import evaluate
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x=randint(0,20)
    y=randint(0,20)
    op=choice(["+","-","*","/"])
    error=randint(-1,1)
    result=evaluate(x,y,op)+error
   
    return x, y, op, result


def check_answer(x, y, op, result, user_choice):
    
    
    if evaluate(x,y,op) == result:
        if user_choice==True:
            return True
        else:
            return False
    else:
        if user_choice==False:
            return True
        else:
            return False
        pass
