from collections import deque

def p(x):
    return -160240/17161 + (30415 * x)/17161 + (15350 * x**2)/17161

print(p(26501365))
exit()

filename = "input.txt"

with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]


    for r,row in enumerate(temp):
        for c,e in enumerate(row):
            if e == 'S':
                start = (r,c)

    #start = (65,0)
    print(start)
    
    Q = deque([(0,start,0,0)])
    num_steps = 65+2*131  # 66 + 131 #131 #,131

    r_max = len(temp)
    c_max = len(temp[0])
    seen = set()
    ret = set()
    while Q:
        step,pos,grid_r,grid_c = Q.popleft()
        if (step,pos,grid_r,grid_c) in seen: continue
        r,c = pos
        seen.add((step,pos,grid_r,grid_c))
        if step == num_steps:
            ret.add((pos,grid_r,grid_c))
            continue
        for rr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_r = r+rr
            new_c = c+cc
            if new_r < 0:
                new_grid_r = grid_r - 1
            elif new_r >= r_max:
                new_grid_r = grid_r + 1
            else:
                new_grid_r = grid_r
            if new_c < 0:
                new_grid_c = grid_c - 1
            elif new_c >= c_max:
                new_grid_c = grid_c + 1
            else:
                new_grid_c = grid_c
            new_r %= r_max
            new_c %= c_max
            if temp[new_r][new_c]!='#':
                Q.append((step+1, (new_r,new_c),new_grid_r,new_grid_c))
        
    ans = len(ret)
    print(ans)
    exit()
    print(ret)
    for r,c in ret:
        temp[r][c] = 'O'
    for row in temp:
        print("".join(row))
