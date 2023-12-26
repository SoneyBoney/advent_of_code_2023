from collections import deque

filename = "test.txt"

ends = set()

def sol(grid, mem, mem_grids, step, pos, grid_r,grid_c):
    global ends
    print(pos, grid_r,grid_c)
    if (step,pos) in mem:
        if (grid_r,grid_c) in mem_grids:
            return 0
        return mem[(step,pos)]
    if step == 0:
        if (pos,grid_r,grid_c) in ends:
            return 0
        ends.add((pos,grid_r,grid_c))
        return 1
    r_max = len(grid)
    c_max = len(grid[0]) 
    ret = 0
    r,c = pos
    for rr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_r = (r+rr)
        new_c = (c+cc)
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
        if grid[new_r][new_c] != '#':
            new_pos = (new_r,new_c)
            ret += sol(grid, mem, mem_grids, step-1, new_pos, new_grid_r,new_grid_c)
    mem[(step,pos)] = ret
    mem_grids.add((grid_r,grid_c))
    return ret
    

with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]


    for r,row in enumerate(temp):
        for c,e in enumerate(row):
            if e == 'S':
                start = (r,c)
    mem = {}
    mem_grids = set()
    steps = 500
    ans = sol(temp, mem, mem_grids, steps, start, 0,0)
    
    print(ans)

    print(ends)
    print(len(ends))
