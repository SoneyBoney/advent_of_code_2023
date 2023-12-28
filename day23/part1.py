import math
import copy
from collections import deque

filename = "input.txt"


def walk_to_fork(grid, pos, seen):
    r_max = len(grid)
    c_max = len(grid[0])
    while True:
        r,c = pos
        if grid[r][c] in "<>^v":
            seen.add(pos)
            if grid[r][c] == '<':
                pos = (r,c-1)
            elif grid[r][c] == '>':
                pos = (r,c+1)
            elif grid[r][c] == '^':
                pos = (r-1,c)
            elif grid[r][c] == 'v':
                pos = (r+1,c)
            continue
        neighbors = []
        for rr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_r = r+rr
            new_c = c+cc
            if 0<=new_r<r_max and 0<=new_c<c_max and (new_r,new_c) not in seen and  grid[new_r][new_c]!='#':
                neighbors.append((new_r,new_c))
        if len(neighbors) != 1:
            return pos,neighbors
        seen.add(pos)
        pos = neighbors[0]
         

def sol(grid, start, end, seen):
    fork_pos,neighbors = walk_to_fork(grid,start,seen)
    if fork_pos == end:
        return len(seen)
    ret = -math.inf      
    for pos in neighbors:
        new_seen = copy.copy(seen)
        temp_sol = sol(grid, pos, end, new_seen)
        ret = max(ret,temp_sol)
    return ret

with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]
    start_c = temp[0].index('.')
    end_c = temp[-1].index('.')
    start = (0,start_c)
    end = (len(temp)-1,end_c)

    seen = set()
    ans = sol(temp, start,end,seen) 
    print(ans)
