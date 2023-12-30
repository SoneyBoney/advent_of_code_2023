import math
import random as rand
import copy
import networkx as nx

filename = "input.txt"



def mc(OG):
    G = copy.deepcopy(OG)
    edges = G.edges
    del_edges = rand.sample((edges), 3)
    G.remove_edges_from(del_edges)
    
    components_gen = nx.connected_components(G)
    components = [x for x in components_gen]
    if len(components) == 2:
        return math.prod([len(x) for x in components])
    return None

def sol(G):
    return nx.minimum_edge_cut(G)


with open(filename) as f:
    temp = f.read().split('\n')[:-1]


    print(temp)
    g = {}
    for ll in temp:
        node_str,edges_str = ll.split(':')

        g[node_str] = [x.strip() for x in edges_str.split() if x]


        
    G = nx.Graph()

    for k,v in g.items():
        G.add_edges_from([(k,vv) for vv in v])
        
    print(G)

    ans2 = sol(G)
    G.remove_edges_from(ans2)
    components_gen = nx.connected_components(G)
    components = [x for x in components_gen]
    ret =  math.prod([len(x) for x in components])
    print(ret)
    exit()

    print(G.edges)
    ans = None
    for _ in range(1000):
        temp = mc(G)
        if temp is not None:
            ans = temp
            break

    print(ans)

