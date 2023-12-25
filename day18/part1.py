import math

filename = "input.txt"


def fill(grid):
    max_r = len(grid)
    max_c = len(grid[0])
    
    start = (0,0)

    Q = [start]
    seen = set()

    while Q:
        r,c = Q.pop(0)
        if (r,c) in seen:
            continue
        grid[r][c] = 'X'
        seen.add((r,c))
        for rr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_r = r+rr
            new_c = c+cc
            if 0 <= new_r < max_r and 0 <= new_c < max_c and grid[new_r][new_c] == '.':
                Q.append((new_r,new_c))
    
    return grid


with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    grid = [['.' for _ in range(500)] for _ in range(500)]

    r_max = -math.inf
    r_min = math.inf
    c_max = -math.inf
    c_min = math.inf
    r_run = 0
    c_run = 0

    pos = (200,200)
    grid[pos[0]][pos[1]] = '#'
    for direction in temp:
        d,steps, _ = direction.split()
        steps = int(steps)

        if d == 'U': 
            r_run -= steps
        elif d == 'D': 
            r_run += steps
        elif d == 'R': 
            c_run += steps
        elif d == 'L': 
            c_run -= steps 
        r_max = max(r_max,r_run)
        r_min = min(r_min, r_run)
        c_max = max(c_max,c_run)
        c_min = min(c_min, c_run)
        

        r,c = pos

        for i in range(1,steps+1):
            if d == 'U': 
                rr = r - i
                cc = c
            elif d == 'D': 
                rr = r + i
                cc = c
            elif d == 'R': 
                rr = r
                cc = c + i
            elif d == 'L': 
                rr = r
                cc = c - i
            if rr < 0 or cc < 0:
                raise RuntimeError("negative")
            grid[rr][cc] = '#'
        pos = (rr,cc)
    

    print('r: ', r_max,r_min)
    print('c: ', c_max,c_min)

    filled_grid = fill(grid)
    ans = 0
    for row in filled_grid:
        for elem in row:
            if elem != 'X':
                ans += 1

    for row in filled_grid:
        print("".join(row)) 

    print(ans)
