import heapq 
import math
filename = "input.txt" 


def is_opposite_dir(a,b):
    if a is None or b is None:
        return False
    if a == b:
        return False
    return abs(a[0]) == abs(b[0]) and abs(a[1]) == abs(b[1])


def sol(m, start, end) -> list:
    max_r = len(m)
    max_c = len(m[0])
    dist = {}
    Q = [(0, start[0], start[1],(1,0),0), (0, start[0], start[1],(0,1),0)]
    heapq.heapify(Q)
    
    seen = set()

    while Q:
        d,r,c,last_dir,dir_count = heapq.heappop(Q)

        if (r,c,last_dir,dir_count) in dist:
            continue
        dist[(r,c, last_dir, dir_count)] = d
        for (rr,cc) in [(1,0),(-1,0),(0,1),(0,-1)]:
            temp_r = r+rr
            temp_c = c+cc
            this_dir = (rr,cc)
            if this_dir == last_dir:
                cur_dir_count = dir_count + 1
            elif dir_count >= 4:
                cur_dir_count = 1
            else:
                continue
            if 0 <= temp_r and temp_r < max_r and 0<=temp_c and temp_c < max_c and cur_dir_count <= 10 and not is_opposite_dir(this_dir,last_dir):
                marginal_dist = m[temp_r][temp_c]
                heapq.heappush(Q, (d+marginal_dist,temp_r,temp_c, this_dir, cur_dir_count))
    return dist
            
with open(filename) as f:
    temp = [[int(x) for x in y] for y in  f.read().split('\n')[:-1]] 


    start = (0,0)
    end = (len(temp)-1,len(temp[0])-1)
    ret = sol(temp, start,end)

    print(ret)
    ans = []
    for k,v in ret.items():
        r,c,last_dir,dir_count = k
        if r == len(temp)-1 and c == len(temp[0])-1:
            ans.append(v)

    print(min(ans))



    
