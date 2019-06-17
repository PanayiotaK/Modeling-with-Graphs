import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    global neighbours
    global visited_counter    
    min_number = min(neighbours)
    neighbours.remove(min_number)
    visited_counter.append(min_number)
    neig_of_vertex = list (G.adj[min_number])
    for neig in neig_of_vertex:
        if neig not in neighbours and neig!=1 and neig not in visited_counter:
            neighbours.append(neig)
    return min_number



def find_smallest_color(G,next_node,colours_used):
    n = len(G.nodes())
    colour=1
    colours_used2= [] 
    colours_used2 = colours_used[:]  
    colours_neig = []
    adj = list(G.adj[next_node])
    for k in adj:
        if G.node[k]['color'] != 'never coloured':
            colours_neig.append(G.node[k]['color'])
    af=list(set(colours_used2)-set(colours_neig))
    af.sort()
    if len(af) > 0:
        colour = af[0]
    else:
        if len(af)==0:
            max_colour = max(colours_neig)
            colour = max_colour+1
   
    return colour
    


neighbours = []
visited_counter = []

def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter 
    global neighbours
    kmax = 0
    neighbours.clear()
    visited_counter.clear()
    colours_used=[]
    G.node[1]['color'] = 1
    neighbours.extend(list(G.adj[1]))
    colours_used.append(1)
    visited_counter.append(1)
    for i in range (1, n):
        next_node = find_next_vertex(G)
        G.node[next_node]['color'] = find_smallest_color(G,next_node,colours_used)
        if G.node[next_node]['color'] not in colours_used:
            colours_used.append(G.node[next_node]['color'])            
    kmax = max(colours_used)
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()


print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


