
filename = "input.txt"




# fill up the string bit by bit
# can memoize from the leftside 
def sol(string, nums, i_string, i_nums, block_len, mem):
    mem_k = (i_string, i_nums, block_len) 
    if mem_k in mem.keys(): return mem[mem_k]
    if len(string) == i_string: 
        # no running blocks
        if i_nums == len(nums) and block_len==0:
            return 1
        elif i_nums == len(nums)-1 and block_len==nums[i_nums]:
            return 1
        return 0
     
    ret = 0
    # case: .: increment to look at next num
    # check to see that current block is valid 
    if block_len and  i_nums <len(nums) and block_len == nums[i_nums] and (string[i_string] == '.' or string[i_string] == '?'): # and c=='.':
        ret += sol(string, nums, i_string+1, i_nums+1, 0,mem)
    # case #: dont increment to look at next num, but increment block len
    if (string[i_string] == '#' or string[i_string] == '?'):
        ret += sol(string, nums, i_string+1, i_nums, block_len+1,mem)
    # case . but block_len ==0, dont increment i_nums
    if block_len == 0 and (string[i_string] == '.' or string[i_string] == '?'): #and c=='.':
        ret += sol(string, nums, i_string+1, i_nums, 0,mem)
    
    mem[mem_k] = ret 
    return ret


with open(filename) as f:
    temp = f.read().split('\n')[:-1]


    temp = [x.split() for x in temp]

    print(temp)
    ret = 0
    for x in temp:
        a,nums = x
        nums = [int(x) for x in nums.split(',')]
        mem = {}
        ret += sol("?".join([a]*5),nums*5, 0, 0, 0,mem)

    print(ret) 
