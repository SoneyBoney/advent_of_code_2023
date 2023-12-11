import math
import numpy as np
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
    len_x = len(m[0])
    len_y = len(m)
    new_map = [['.']*len_x*3 for _ in range(len_y*3)]
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
        x = current_pos[0] 
        y = current_pos[1]
        temp_shape = m[x][y]
        if temp_shape == "|":
            new_map[x*3-1][y*3] = 'X'
            new_map[x*3][y*3] = 'X'
            new_map[x*3+1][y*3] = 'X'
        if temp_shape == "-":
            new_map[x*3][y*3-1] = 'X'
            new_map[x*3][y*3] = 'X'
            new_map[x*3][y*3+1] = 'X'
        if temp_shape == "L":
            new_map[x*3][y*3+1] = 'X'
            new_map[x*3][y*3] = 'X'
            new_map[x*3-1][y*3] = 'X'
        if temp_shape == "7":
            new_map[x*3][y*3-1] = 'X'
            new_map[x*3][y*3] = 'X'
            new_map[x*3+1][y*3] = 'X'
        if temp_shape == "J":
            new_map[x*3-1][y*3] = 'X'
            new_map[x*3][y*3] = 'X'
            new_map[x*3][y*3-1] = 'X'
        if temp_shape == "F":
            new_map[x*3+1][y*3] = 'X'
            new_map[x*3][y*3] = 'X'
            new_map[x*3][y*3+1] = 'X'
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
    return new_map

def find_area(m):
    # interior is a connected component so just find
    # a starting point in the exterior and just bfs and take complement
    q = []
    for i in [0,-1]:
        for j in range(len(m[0])):
            if m[i][j] == '.':
                q.append((i,j))
        for j in range(len(m)):
            if m[j][i] == '.':
                q.append((j,i))

    i_max = len(m[0])-1
    j_max = len(m)-1
    while q:
        pos = q.pop(0)
        i,j =  pos
        try:
            if m[i][j] == 'X':
                continue
            if m[i][j] == 'Y':
                continue
            m[i][j] = 'Y'
            if i-1 >= 0:
                q.append((i-1,j))
            if i+1 <= i_max:
                q.append((i+1,j))
            if j-1 >= 0:
                q.append((i,j-1))
            if j+1 <= j_max:
                q.append((i,j+1))
        except IndexError:
            continue
    ret = 0 
    for i,row in enumerate(m):
        for j,e in enumerate(row):
            if e == '.':
                if is_interior(m, (i,j)):
                    ret += 1
    for row in m:
        print("".join(row))
    return ret / 9

def is_interior(m, ind):
    x,y = ind
    try:
        for i in [0,1,-1]:
            for j in [0,1,-1]:
                if m[x+i][y+j] != '.':
                    return False    
    except IndexError:
        return False
    return True 


with open(filename) as f:
    temp = f.read().split('\n')[:-1]
    # find S
    for i,row in enumerate(temp):
        j = row.find('S')
        if j != -1:
            start = (i,j)
    m = [list(x) for x in temp]

    for shape in "|-JL7F":
        try:
            ret = traverse(m,start,shape)
        except RuntimeError as e:
            print(e)
            continue
    for row in ret:
        print("".join(row))
    print()
    a = find_area(ret)
    print(a)
