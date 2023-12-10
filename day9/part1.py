
filename = "input.txt"



def sol(num_list):
    ret = []
    ret.append(num_list)
    temp = num_list
    while any(temp):
        temp_list = [b-a for a,b in zip(temp[0::],temp[1::])]
        ret.append(temp_list)
        temp = temp_list
    ret[-1].append(0) 
    
    for i in range(len(ret)-2, -1,-1):
        last_val = ret[i][-1]
        diff = ret[i+1][-1]
        ret[i].append(last_val+diff)

    print(ret)
    return ret[0][-1]



with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    nums = [[int(n) for n in x.split()] for x in temp]

    ans = 0
    for val in nums:
        ans += sol(val)

    print(ans)
