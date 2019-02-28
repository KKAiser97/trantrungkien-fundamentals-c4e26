from random import *
from is_inside import is_inside
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    

    return [
                text,
                color,
                quiz_type, # 0 : meaning, 1: color
                
            ]
text=shapes[randint(0,3)]["text"]
print(text)
color=shapes[randint(0,3)]["text"]
print(color)
quiz_type=randint(0,1)
    
# user_answer=is_inside.is_inside(x,y)
def mouse_press(x, y, text, color, quiz_type):

    pos= [x, y]
    for i in range(4):
        if is_inside(pos, shapes[i]["rect"]) == True:
            user_answer = [shapes[i]["text"], shapes[i]["color"]]
    if quiz_type == 0:
        if user_answer[0] == text:
            return True
        else:
            return False
    else:
        if user_answer[1] == color:
            return True
        else:
            return False