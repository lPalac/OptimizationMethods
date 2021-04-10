import networkx as nx
import matplotlib.pyplot as plt
import time

def citanjePajek(folderName):
    G = nx.read_pajek(folderName)
    return G

def crtanjeGrafa(G):
    plt.subplot(111)
    nx.draw_circular(G, with_labels = True, font_weight="bold")
    plt.show()

def dijkstraAlgoritam(G, source):
    for target in G.nodes:
        if target != source:
            najkraciPut = nx.shortest_path(G, source, target, weight= "string") #defoltni tragac je dijkstra
            print(list(najkraciPut))

    
def bellmanFordAlgoritam(G, source):
    for target in G.nodes:
        if target != source:
            najkraciPut = nx.shortest_path(G, source, target, weight= "string", method="bellman-ford")
            print(list(najkraciPut))

def main():

    G = citanjePajek("airports-split.net")

    crtanjeGrafa(G) #ovo sam samo iz zabave napravija

    start = time.time()
    najkraciPut= dijkstraAlgoritam(G, "MAD") #a
    print(time.time() - start, "sekundi")

    start = time.time()
    najkraciPut= bellmanFordAlgoritam(G, "MAD") #b
    print(time.time() - start, "sekundi")

if __name__=='__main__':
    main()