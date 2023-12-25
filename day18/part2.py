import math

filename = "input.txt"


def decode(code):
    str_code = code[2:-1]

    meters = int(str_code[:5],16)
    dd = str_code[-1]

    if dd=='0':
        d = 'R'
    elif dd =='1':
        d = 'D'
    elif dd=='2':
        d = 'L'
    else:
        d = 'U'
    return d,meters

with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    boundary = 0
    interior = 0
    y = 1186328
    y_min = math.inf
    for direction in temp:
        _,_,code = direction.split()
        d,steps = decode(code)
    
        print(d,steps)
        boundary += steps
        if d == 'U':
            y += steps
        elif d == 'D': 
            y -= steps
        elif d == 'R': 
            interior += y*steps
        elif d == 'L': 
            interior -= y*steps

        y_min = min(y_min,y)
    total = interior + boundary//2 + 1
    
    print(total)
    
    print(y_min)

