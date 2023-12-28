import networkx as nx
import math
import copy
from collections import deque

filename = "input.txt"
fork_mem = {}


def get_all_forks(grid):
    ret = []
    r_max = len(grid)
    c_max = len(grid[0])
    steps = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            elem = grid[r][c]
            if elem == '#': continue
            neighbors = 0
            for rr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r = r + rr
                new_c = c + cc
                if 0<=new_r<r_max and 0<=new_c<c_max and grid[new_r][new_c] != '#':
                    neighbors += 1
            if neighbors >= 3: # is a fork (original position is also a neighbor)
                ret.append((r,c))
    return ret

def get_edge_weights(grid, forks):
    r_max = len(grid)
    c_max = len(grid[0])
    ret = {node: {} for node in forks}
    for start in forks:
        Q = [(start,0)]
        seen = set([start])
        while Q:
            pos,steps = Q.pop()
            r,c = pos
            if steps != 0 and pos in forks:
                ret[start][pos] = steps
                continue
            for rr,cc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = r + rr
                new_c = c + cc
                if 0 <= new_r < r_max and 0 <= new_c < c_max and grid[new_r][new_c] != '#' and (new_r,new_c) not in seen:
                    new_pos = (new_r,new_c)
                    Q.append((new_pos,steps+1))
                    seen.add(new_pos)
    return ret
 

def find_longest_path(edges, start, end, seen):
    if start == end:
        return 0
    
    ret = -math.inf
    current_node_info = edges[start]
    seen.add(start) # to prevent cycles
    for neighbor,weight in current_node_info.items():
        if neighbor not in seen:
            ret = max(ret,find_longest_path(edges, neighbor, end,seen)+weight)
    seen.remove(start)
    return ret
    

with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]
    start_c = temp[0].index('.')
    end_c = temp[-1].index('.')
    start = (0,start_c)
    end = (len(temp)-1,end_c)


    fork_points = get_all_forks(temp)
    fork_points = [start,end] + fork_points
    
    edges = get_edge_weights(temp, fork_points)
    print(edges)

    seen = set()
    ans = find_longest_path(edges, start, end, seen)
    print(ans)
