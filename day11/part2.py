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

def count_empty_rows(m, start, end):
    count = 0
    for r in range(start,end+1):
        row = m[r]
        if all([x=='.' for x in row]):
            count+=1
    return count
    


def manhattan_distance(a,b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def sol(m,index_map):
    ret = 0
    seen = set()
    print(f"num galaxies: {len(index_map.keys())}") 
    count = 0
    for a,a_val in index_map.items():
        for b,b_val in index_map.items():
            if (b,a) not in seen:
                print(count)
                temp = manhattan_distance(a_val,b_val)
                empty_rows = count_empty_rows(m, min(a_val[0],b_val[0]), max(a_val[0],b_val[0]))
                empty_cols = count_empty_rows(transpose(m), min(a_val[1],b_val[1]), max(a_val[1],b_val[1])) 
                temp -= empty_rows + empty_cols
                temp += 1000000*(empty_rows + empty_cols)
                ret += temp
                seen.add((a,b))
                count +=1
    return ret
            

with open(filename) as f:
    temp = f.read().split('\n')[:-1]
    temp = [list(x) for x in temp] 
    count = 1
    index_map = {}
    for i,row in enumerate(temp):
        for j,elem in enumerate(row):
            if elem == '#':
                temp[i][j] = str(count)
                count += 1
                index_map[str(count)] = (i,j)
    ans = sol(temp,index_map)

    print(ans)





    
