from collections import deque

filename = "input.txt"

with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]


    for r,row in enumerate(temp):
        for c,e in enumerate(row):
            if e == 'S':
                start = (r,c)
    print(start)
    
    Q = deque([(0,start)])
    num_steps = 64 #130,131

    r_max = len(temp)
    c_max = len(temp[0])
    seen = set()
    ret = set()
    while Q:
        step,pos = Q.popleft()
        if (step,pos) in seen: continue
        r,c = pos
        seen.add((step,pos))
        if step == num_steps:
            ret.add(pos)
            continue
        for rr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_r = r+rr
            new_c = c+cc
            if 0 <= new_r < r_max and 0<=new_c<c_max and temp[new_r][new_c]!='#':
                Q.append((step+1, (new_r,new_c)))
        
    ans = len(ret)
    print(ret)
    for r,c in ret:
        temp[r][c] = 'O'
    for row in temp:
        print("".join(row))
    print(ans)
