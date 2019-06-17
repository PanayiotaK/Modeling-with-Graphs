import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G,i,colours_used):
    colour=1
    n = len(G.nodes())
    colours_available= [] 
    colours_available = colours_used[:]  
    colours_neig = []
    af = []
    if i == 1:
        colour = 1
        return colour
    else:
        neighbours = list(G.adj[i])
        for j in range(len(neighbours)-1,-1,-1):
            if neighbours[j]>i:
                neighbours.remove(neighbours[j])
        for k in neighbours:
            colours_neig.append(G.node[k]['color'])
        af=list(set(colours_available)-set(colours_neig))
        af.sort()
        if len(af) > 0:
            colour = af[0]
        else:
            if len(af)==0:
                max_colour = max(colours_neig)
                colour = max_colour+1
   
    return colour


def greedy(G):
    global kmax
    colours_used=[]
    for i in range(1,G.number_of_nodes()+1):
        col = find_smallest_color(G,i,colours_used)
        if col not in colours_used:
            colours_used.append(col)
        G.node[i]['color'] = col
    kmax = max(colours_used)
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)



print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)


