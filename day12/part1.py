
filename = "test.txt"




def sol(a, nums):
    if '?' not in a:
        temp = [len(x) for x in a.split('.') if x]
        if temp == nums:
            print(f"adding: {a}, {nums}")
            return 1
        return 0
    return sol(a.replace('?', '#', 1),nums) + sol( a.replace('?', '.', 1),nums)
        


with open(filename) as f:
    temp = f.read().split('\n')[:-1]


    temp = [x.split() for x in temp]

    print(temp)
    ret = 0
    for x in temp:
        a,nums = x
        nums = [int(x) for x in nums.split(',')]
        ret += sol(a,nums)

    print(ret) 
