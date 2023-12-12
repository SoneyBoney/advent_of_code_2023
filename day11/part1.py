import copy
import math

filename = "input.txt"


def transpose(m):
    len_R = len(m)
    len_C = len(m[0])
    m2 = [[None for _ in range(len_R)] for _ in range(len_C)]
    for i in range(len_R):
        for j in range(len_C):
            m2[j][i] = m[i][j]
    return m2

def warp(m):
    m2 = []
    for row in m:
        if all([x=='.' for x in row]):
            m2.append(row)
            m2.append(row)
        else:
            m2.append(row)
    m2 = transpose(m2)
    m3 = [] 
    for row in m2:
        if all([x=='.' for x in row]):
            m3.append(row)
            m3.append(row)
        else:
            m3.append(row)
    ret = transpose(m3)
    return ret
            


def floyd_warshal(m, V):
    num_V = len(V)
    dist = [[math.inf for _ in range(num_V)] for _ in range(num_V)]

def manhattan_distance(a,b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def sol(index_map):
    ret = 0
    seen = set()
    for a,a_val in index_map.items():
        for b,b_val in index_map.items():
            if (b,a) not in seen:
                ret += manhattan_distance(a_val,b_val)
                seen.add((a,b))
    return ret
            

with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    warped_map = warp(temp)

    count = 1
    index_map = {}
    for i,row in enumerate(warped_map):
        for j,elem in enumerate(row):
            if elem == '#':
                warped_map[i][j] = str(count)
                count += 1
                index_map[str(count)] = (i,j)
    ans = sol(index_map)

    print(ans)





    
