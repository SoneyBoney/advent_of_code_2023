
from pprint import pprint
import copy

filename = "test.txt"



def params_to_intervals(params):
    params = [[int(x) for x in y.split(' ')] for y in params]
    ret = {}
    for p in params:
        dest_start = p[0] 
        source_start = p[1]
        range_len = p[2]-1
        ret[(source_start,source_start+range_len)] = (dest_start,dest_start+range_len)
    return ret


def splice(a,b):
    if a[1] < b[0] or a[0] > b[1]:
        return [a]
    ret = []
    left = (a[0], b[0]-1)
    if left[1] - left[0] >= 0:
        ret.append(left)
    right = (b[1]+1, a[1])
    if right[1] - right[0] >= 0:
        ret.append(right)
    return ret

def apply(func: dict, n):
    for k,v in func.items():
        if k[0] <= n and n <= k[1]:
            return n - k[0] + v[0]
    return n

with open(filename) as f:
    temp = f.read().split('\n\n')[:-1]

    seed_str = temp[0]
    temp2 = temp[1:]

    compose_ints = None
    debug = 0
    for mapping in temp2[::-1]:
        debug += 1
        map_temp = mapping.split('\n')
        params = map_temp[1:]
        intervals = params_to_intervals(params)
        if not compose_ints:
            compose_ints = intervals
            continue 
        #for source,target in compose_ints.items():
        Q = copy.deepcopy(list(compose_ints.items()))
        while Q:
            target_k,target_v = Q.pop(0)
            disjoint_count = 0
            interval_count = len(intervals.items())
            # compose with target intervals from "intervals"
            for k,v in intervals.items():
                if v[1] < target_k[0] or target_k[1] < v[0]:
                    disjoint_count += 1
                else:
                    overlap = (max(target_k[0],v[0]),min(target_k[1],v[1]))
                    overlap_range = overlap[1]-overlap[0]
                    overlap_out_start = overlap[0] - target_k[0] + target_v[0]
                    overlap_out = (overlap_out_start, overlap_out_start+overlap_range)
                    overlap_key_start = overlap[0] - v[0] + k[0]
                    overlap_key = (overlap_key_start,overlap_key_start+overlap_range)
                    compose_ints[overlap_key] = overlap_out

                    target_complement = splice(target_k, overlap)
                    for tc in target_complement:
                        target_range = tc[1] - tc[0]
                        target_out_start = tc[0] - target_k[0] + target_v[0]
                        Q.append((tc, (target_out_start,target_out_start+target_range)))
                    try:
                        del compose_ints[target_k]
                    except KeyError as e:
                        pass
            if disjoint_count == interval_count: 
                compose_ints[target_k] = target_v
        temp_items = copy.deepcopy(list(compose_ints.items()))
        for interval_k,interval_v in intervals.items():
            disjoint_num = 0
            temp_complements = [interval_v]
            for compose_k,compose_v in temp_items:
                if interval_v[1] < compose_k[0] or compose_k[1] < interval_v[0]: 
                    disjoint_num += 1
                else:
                    temp2 = []
                    for x in temp_complements:
                        temp3 = splice(x,compose_k)
                        if temp3:
                            temp2 += temp3
                    temp_complements = temp2
            if disjoint_num == len(temp_items):
                compose_ints[interval_k] = interval_v
            for sc in temp_complements:
                sc_range = sc[1]-sc[0]
                sc_key_start = sc[0]-interval_v[0] + interval_k[0]
                sc_key = (sc_key_start,sc_key_start+sc_range)
                compose_ints[sc_key] = sc

    ret = []
    seed_str = seed_str.removeprefix('seeds: ').strip()
    seed_str_split = seed_str.split()
    for i,seed in enumerate(seed_str_split[::2]):
        for j in range(int(seed),int(seed)+int(seed_str_split[i+1])):
            ret.append(apply(compose_ints,int(j))) 

    print(ret)
    print(min(ret))
    
    pprint(compose_ints)


