
filename = "input.txt"

def transpose(m):
    len_R = len(m)
    len_C = len(m[0])
    m2 = [[None for _ in range(len_R)] for _ in range(len_C)]
    for i in range(len_R):
        for j in range(len_C):
            m2[j][i] = m[i][j]
    return m2

def num_diff(a,b):
    ret = sum([1 for x,y in zip(a,b) if x!=y])
    return ret

def helper(a):
    for i,row in enumerate(a[:-1]):
        #if row == a[i+1]:
        temp = [num_diff(a[i-j],a[i+j+1]) for j in range(min(i+1,len(a)-i-1))]
        if sum(temp) == 1:
            return i+1
             
def sol(a):
    ret = helper(a)
    if ret: return 100*ret
    return helper(transpose(a))


with open(filename) as f:
    temp = [x.split('\n') for x in f.read().split('\n\n')[:-1]]

    
    ans = 0 
    for pattern in temp:
        ans += sol(pattern)
            

    print(ans)
