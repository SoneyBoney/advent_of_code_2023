import copy
import math

filename = "input.txt"



def gen_mapping(network):
    ret = {}
    for mapping in network:
        key, val = mapping.split(" = ")	
        a,b = val[1:-1].split(', ')
        ret[key] = (a,b)
    return ret
        

with open(filename) as f:
    temp = [x for x in f.read().split('\n') if x]

    instructions = temp[0]

    network = temp[1:]

    mappings = gen_mapping(network)
    start_nodes = [x for x in mappings.keys() if x.endswith('A')]
    temp_nodes = copy.deepcopy(start_nodes)
    mem = {} 
    print(start_nodes)
    inst_ind = 0
    count = 0
    while True:
        direction = instructions[inst_ind]
        if direction == 'R':
            ind = 1
        else:
            ind = 0
        for i,node in enumerate(start_nodes):
            temp = mappings[node][ind]
            if temp.endswith('Z'):
                if temp_nodes[i] not in mem.keys():
                    mem[temp_nodes[i]] = count+1
                print(f"{temp_nodes[i]}: {count}")
            start_nodes[i] = mappings[node][ind]
        inst_ind = (inst_ind + 1) % len(instructions)
        count += 1
        if len(mem.keys()) == len(start_nodes):
            break       
    print(mem)
    print(math.lcm(*list(mem.values())))




