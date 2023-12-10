
filename = "input.txt"



def gen_mapping(network):
    ret = {}
    for mapping in network:
        key, val = mapping.split(" = ")	
        a,b = val[1:-1].split(', ')
        ret[key] = (a,b)
    print(ret)
    return ret
        

with open(filename) as f:
    temp = [x for x in f.read().split('\n') if x]


    print(temp)

    instructions = temp[0]

    network = temp[1:]

    mappings = gen_mapping(network)

    start = 'AAA'
    end = 'ZZZ'

    inst_ind = 0
    count = 0
    while start != end:
        direction = instructions[inst_ind]
        if direction == 'R':
            ind = 1
        else:
            ind = 0	    
        start = mappings[start][ind]
        inst_ind = (inst_ind + 1) % len(instructions)
        count += 1
    print(count)


