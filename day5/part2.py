
from pprint import pprint
import copy

filename = "input.txt"


def apply(specs, intervals):
    ret = []
    for p in specs:
        save = []
        while intervals:
            current_int = intervals.pop(0)
            target_start,domain_start,r = p
            domain_interval = (domain_start, domain_start+r)
            if current_int[1] < domain_interval[0] or domain_interval[1] < current_int[0]:
                save.append(current_int)
                continue
            if current_int[0] < domain_interval[0]:
                left = (current_int[0], domain_interval[0])
                save.append(left)
            if current_int[1] > domain_interval[1]:
                right = (domain_interval[1], current_int[1])
                save.append(right)
            overlap = (max(current_int[0],domain_interval[0]), min(current_int[1],domain_interval[1]))
            if overlap[1] - overlap[0] > 0:
                ret.append((overlap[0]-domain_start+target_start,overlap[1]-domain_start+target_start))
        intervals = save
    return ret + intervals


with open(filename) as f:
    temp = f.read().split('\n\n')[:-1]

    seeds = [int(x) for x in temp[0].removeprefix('seeds: ').split()]
    temp = [[[int(z) for z in y.split()] for y in x.split('\n')[1:]] for x in temp[1:]]

    print(seeds)
    seed_intervals = [(x,x+y) for x,y in zip(seeds[::2],seeds[1::2])]

    ret = []
    for si in seed_intervals:
        intervals = [si]
        for specs in temp:
            intervals = apply(specs,intervals)
        ret += intervals

    print(min(ret,key=lambda x: x[0])[0])
