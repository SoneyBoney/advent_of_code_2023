import math

filename = "input.txt"



def gen_distance(time_limit, hold_time):
    v = hold_time
    time_left = time_limit - hold_time
    d = time_left * v
    return d

def get_all_distances(time_limit):
    ret = [gen_distance(time_limit, t) for t in range(time_limit)] 

    return ret
    
    


with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    times = [int(x) for x in temp[0].removeprefix('Time:').strip().split() if x]

    ret = [get_all_distances(t) for t in times]

    print(ret)

    distance_records = [int(x) for x in temp[1].removeprefix('Distance:').strip().split() if x]

    ans = [[x for x in ret[i] if x>d]  for i,d in enumerate(distance_records)]

    answer = math.prod([len(x) for x in ans])

    print(answer)
