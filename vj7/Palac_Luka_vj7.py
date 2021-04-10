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

def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def dodajUdaljenosti(G,target):
    brojacKategorija = 0 #Verticels = 1, Arcs = 2, Edges = 3. 
    verticels = []
    koordinate = []
    
    with open("airports-astar.net", "r") as inputfile:
        for line in inputfile:
            if("*" in line): #Dize broj 
                brojacKategorija += 1 
            elif brojacKategorija == 1:#Verticels = 1
                verticels.append(line.split())
        for i in verticels:
            if i[1] == target:  #malo sam rasirija da se bolje vidit 
                xt = int(i[2])
                yt = int(i[3]) 
                t= (xt,yt)
                for j in verticels:
                    x = int(j[2])
                    y = int(j[3])
                    s= (x,y)                   
                    k= {j[1]: dist(s,t)} # nači ce udaljenosti broj i dodat na key to mozemo vidijetu u G.nodes._nodes 
                    
                    
                    nx.set_node_attributes(G,values=k,name="name")


def aStarAlgoritam(G,source, target):

    dodajUdaljenosti(G,target)
    
    najkraciPut = nx.astar_path(G, source, target,heuristic= dist(source,target) ,weight="name") # 
    print(list(najkraciPut))
    return najkraciPut

    
def greedyBFSAlgoritam(G, source, target):
    najkraciPut = nx.single_target_shortest_path(G, target ,cutoff=None)
    print(list(najkraciPut[source]))
    return najkraciPut

def main():

    G = citanjePajek("airports-astar.net")

    crtanjeGrafa(G) #ovo sam samo iz zabave napravija

    
    source = input("Unesite start puta (npr. MAD)")
    target = input("Unesite zavrsetak puta (npr. ARN)") # na ova dva grada cemo vidijeti razliku izmedu ova dva algoritma pretrazivanja
    
    start = time.time()
    najkraciPut= greedyBFSAlgoritam(G, source, target) #a
    print(time.time() - start, "sekundi")
    
    start = time.time()
    najkraciPut= aStarAlgoritam(G, source, target) #b
    print(time.time() - start, "sekundi")

if __name__=='__main__':
    main()