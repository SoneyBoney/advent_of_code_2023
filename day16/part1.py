
filename = "input.txt"




def step(m, pos, d):
    r_max = len(m)-1
    c_max = len(m[0])-1
    r,c = pos
    if d == 'U':
        new_r = r-1
        new_c = c
    elif d == 'D':
        new_r = r+1
        new_c = c
    elif d == 'L':
        new_r = r
        new_c = c-1
    elif d== 'R':
        new_r = r
        new_c = c+1
    else:
        raise RuntimeError("should not happen")
    if new_r < 0 or new_r > r_max or new_c < 0 or new_c > c_max:
        return None
    return (new_r,new_c)


def sim(m, p, d):
    
    m_copy = [['.' for _ in range(len(m[0]))] for _ in range(len(m))]
    
    p_list = [(p,d)]
    seen = set()
    
    while p_list:
        p_item = p_list.pop(0)
        while p_item:
            if p_item in seen:
                break
            p,d = p_item
            r,c = p
            m_copy[r][c] = 'X'
            symbol = m[r][c]
            if symbol == '.':
                pass
            if symbol == '/':
                if d == 'R': d = 'U'
                elif d == 'L': d = 'D'
                elif d == 'U': d = 'R'
                elif d == 'D': d = 'L'
            if symbol == '\\':
                if d == 'R': d = 'D'
                elif d == 'L': d = 'U'
                elif d == 'U': d = 'L'
                elif d == 'D': d = 'R'
            if symbol == '-':
                if d in 'RL': pass
                elif d in 'UD': 
                    p_list.append((p,'L'))
                    d = 'R'
            if symbol == '|':
                if d in 'UD': pass
                elif d in 'RL':
                    p_list.append((p,'U'))
                    d = 'D'
            next_pos = step(m,p,d)
            seen.add(p_item)
            p_item = (next_pos,d) if next_pos else None
                 
    return m_copy
    




with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]

    start_configs = []

    for i in range(len(temp[0])):
        start_configs.append(((0,i), 'D'))
    for i in range(len(temp[0])):
        start_configs.append(((len(temp)-1,i), 'U'))
    for i in range(len(temp)):
        start_configs.append(((i,0), 'R'))
    for i in range(len(temp)):
        start_configs.append(((i,len(temp)-1), 'L'))
             
    ans_list = []
    for sc in start_configs:
        p,d = sc
        energy_map = sim(temp,p,d)
        ans = 0
        for row in energy_map:
            for elem in row:
                if elem == 'X':
                    ans += 1
        ans_list.append(ans)
    print(ans_list)
    print(max(ans_list))
