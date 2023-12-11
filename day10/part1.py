import math
from enum import Enum
import copy 

filename = "input.txt"


def step(m, pos, prev):
    current_shape = m[pos[0]][pos[1]]
    if current_shape == '|':
        print(prev,pos)
        if prev[0] < pos[0]:
            next_pos = (pos[0]+1,pos[1]) 
        elif prev[0] > pos[0]:
            next_pos = (pos[0]-1,pos[1]) 
        else:
            print(f"Shape: {current_shape}, prev: {prev}, current: {pos}")
            raise RuntimeError("should not happen")
    elif current_shape == '-':
        if prev[1] > pos[1]:
            next_pos = (pos[0],pos[1]-1)
        elif prev[1] < pos[1]:
            next_pos = (pos[0],pos[1]+1)
        else:
            print(f"Shape: {current_shape}, prev: {prev}, current: {pos}")
            raise RuntimeError("should not happen")
    elif current_shape == 'L':
        if prev[0] < pos[0]:
            next_pos = (pos[0],pos[1]+1)
        elif prev[1] > pos[1]:
            next_pos = (pos[0]-1,pos[1])
        else:
            print(f"Shape: {current_shape}, prev: {prev}, current: {pos}")
            raise RuntimeError("should not happen")
    elif current_shape == 'J':
        if prev[0] < pos[0]:
            next_pos = (pos[0],pos[1]-1)
        elif prev[1] < pos[1]:
            next_pos = (pos[0]-1,pos[1])
        else:
            print(f"Shape: {current_shape}, prev: {prev}, current: {pos}")
            raise RuntimeError("should not happen")
    elif current_shape == '7':
        if prev[0] > pos[0]:
            next_pos = (pos[0],pos[1]-1)
        elif prev[1] < pos[1]:
            next_pos = (pos[0]+1,pos[1])
        else:
            print(f"Shape: {current_shape}, prev: {prev}, current: {pos}")
            raise RuntimeError("should not happen")
    elif current_shape == 'F':
        if prev[0] > pos[0]:
            next_pos = (pos[0],pos[1]+1)
        elif prev[1] > pos[1]:
            next_pos = (pos[0]+1,pos[1])
        else:
            print(f"Shape: {current_shape}, prev: {prev}, current: {pos}")
            raise RuntimeError("should not happen")
    else:
        return None
    return next_pos

def traverse(matrix, start, shape):
    m = copy.deepcopy(matrix)
    print(shape) 
    m[start[0]][start[1]] = shape
    if shape == '|':
        prev = (start[0]-1,start[1])
    elif shape == '-':
        prev = (start[0],start[1]-1)
    elif shape == 'L':
        prev = (start[0]-1,start[1])
    elif shape == 'J':
        prev = (start[0]-1,start[1])
    elif shape == '7':
        prev = (start[0]+1,start[1])
    elif shape == 'F':
        prev = (start[0]+1,start[1])
    current_pos = start
    seen = set()
    count = 0
    while True:
        print(current_pos)
        temp = step(m, current_pos, prev)
        prev = current_pos
        current_pos = temp
        count += 1
        if current_pos == start:
            print('hi', )
            # check if we can keep stepping to make sure that it forms a loop
            step(m, current_pos, prev)
            break
        if current_pos in seen:
            raise RuntimeError("bad loop")
        seen.add(current_pos) 

    return math.ceil(count/2)


        

    


with open(filename) as f:
    temp = f.read().split('\n')[:-1]


    print(temp)


    # find S
    for i,row in enumerate(temp):
        j = row.find('S')
        if j != -1:
            start = (i,j)
    m = [list(x) for x in temp]
    ret = []
    for shape in "|-JL7F":
        try:
            ret.append(traverse(m, start, shape))
        except RuntimeError as e:
            print(e)
            continue

    print(ret)
