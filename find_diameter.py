import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10


def bfs(G,a):
    length_graph=len(G.nodes())
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.node[a]['label'] = 0
    i = 0
    neig = []
    counter = 1
    max_d = 0
    while counter< length_graph:        
        for j in range (1,G.number_of_nodes()+1):
            if G.node[j]['label'] == i:                
                neig.extend(list(G.adj[j]))
                for n in neig:
                    if G.node[n]['label'] == -1:
                        G.node[n]['label'] = i+1                        
                        counter += 1
                        if G.node[n]['label']> max_d:
                            max_d = G.node[n]['label']                        
        i+= 1
    return max_d





def max_distance(G):
    diame= []
    for i in range (1,G.number_of_nodes()+1):
        diame.append(bfs(G,i))
        
    return max(diame)
    

print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()


