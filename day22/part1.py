from pprint import pprint
import bisect
import sys
import copy

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "test.txt"


def intersect(a,b):
    return (b[0] <= a[0] <= b[3] or a[0] <= b[0] <= a[3]) and (b[1] <= a[1] <= b[4] or a[1] <= b[1] <= a[4])

def gravity(all_blocks):
    all_blocks.sort(key=lambda x: x[5]) 
    for i,b in enumerate(all_blocks):
        target_z = 1
        for other in all_blocks[:i]:
            if intersect(b,other):
                target_z = max(target_z, other[5]+1)
        #z_len = b[5] - b[2]
        #b[2] = target_z
        #b[5] = b[2] + z_len
        b[5] -= b[2] - target_z
        b[2] = target_z
    all_blocks.sort(key=lambda x: x[2])
    return all_blocks
        
def create_graph(blocks):
    children = {i : set() for i in range(len(blocks))}
    parents = {i : set() for i in range(len(blocks))}

    for i,b1 in enumerate(blocks):
        for j,b2 in enumerate(blocks):
            if i == j:
                continue
            if intersect(b1,b2) and b2[5]==b1[2]-1:
                children[i].add(j)
                parents[j].add(i)
    return children,parents
         

with open(filename) as f:
    temp = f.read().split('\n')[:-1]
    blocks = []
    
    for line in temp:
        start_str,end_str = line.split('~')
        sx,sy,sz = [int(x) for x in start_str.split(',')]
        ex,ey,ez = [int(x) for x in end_str.split(',')]
        block = [sx,sy,sz,ex,ey,ez]
        blocks.append(block)

    blocks = gravity(blocks)
    print(blocks)
    G_children,G_parents = create_graph(blocks)
    pprint(G_children)
    
    ans = 0

    for node,_ in G_children.items():
        parents = G_parents[node]
        parents_supported = [len(G_children[p]) > 1 for p in parents]
        if all(parents_supported):
            ans += 1

    print(ans)
