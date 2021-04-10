import csv
import random
from itertools import permutations  
import copy
import time

def readCSV():
    with open("distanceManji.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        svePutanje = {}
        putanje = {}

        for row in reader:
            for i in row:
                if row[i]!= "-" and i!="": # da preskocimo ako je prvi clan ili sa samin sobom
                    putanje[i] = row[i] # stavi u dict "putanja[row][i]"
                elif i=="":
                    red = row[i] # sprema redak u kojem smo
            svePutanje[red]=putanje
            putanje = {}

    return svePutanje

def bruteForce(svePutanje):
    najkraciPut=[]
    akumulator = 0
    minPutanja = 0
    start = random.choice(list(svePutanje.keys())) #random start
    korak = start
    print ("Počinjemo iz", korak)
    putanja = svePutanje[korak] # da koristimo samo onu koju smo startali ostale su nam nepotrebne

    perm = permutations(putanja)  
    for i in list(perm):  
        for j in range(len(i)):
            akumulator += int(svePutanje[i[j]][korak]) #najbolji put
            korak = i[j]
        korak = start

        if akumulator < minPutanja:
            minPutanja = akumulator
            najkraciPut = i
        elif minPutanja == 0:
            minPutanja = akumulator
            najkraciPut = i
        akumulator = 0  


    najkraciPut = najkraciPut + (start, ) # dodajem radi ljepske izgleda 
    print ("Najbolja putanja je =",najkraciPut)
    print("Putanja je duga",minPutanja)
    return najkraciPut

def najblizegSusjeda(svePutanje):
    najkraciPut=[]
    akumulator = 0
    start = random.choice(list(svePutanje.keys())) #random start
    korak = start
    print ("Počinjemo iz", korak)
    nismoProsli = copy.deepcopy(svePutanje) #iz neznan kojeg razloga obicni copy nije radio nismoProsli = svePutanje.copy()
    prosli = 1
    for i in range(len(nismoProsli[korak])):  
        
        for j in nismoProsli:    
            if korak in nismoProsli[j]:
                nismoProsli[j].pop(korak)

        najmanjiKljuc= nadiNajmanjiKljuc(nismoProsli[korak])

        #najmanjiKljuc= min(nismoProsli[korak], key=nismoProsli[korak].get) #minimalni do odredenog puta zanima 
         # me zasto ovo mi ne vraca najmanji ali nije bitno napisa sam sam svoju funkciju
        
        akumulator += int(nismoProsli[korak][najmanjiKljuc])

        najkraciPut.append(najmanjiKljuc)#za krajni ispis
        korak = najmanjiKljuc 

    akumulator += int(svePutanje[korak][start])
    najkraciPut.append(start)

    print ("Najbolja putanja je =",najkraciPut)
    print("Putanja je duga",akumulator)
    return najkraciPut

def nadiNajmanjiKljuc(putanja): #koristi se u zad.2
    najmanjaPutanja = 0
    for i in putanja:
        if (int(putanja[i]) < najmanjaPutanja):
            najmanjaPutanja=int(putanja[i])
            najmanjiKljuc = i
        elif najmanjaPutanja == 0:
            najmanjaPutanja = int(putanja[i])
            najmanjiKljuc = i
    

    return najmanjiKljuc


def sortiranihBridova(svePutanje):
    grafBridova = {}
    edges = []
    edges = konverzijaGrafUListu(svePutanje)
    
    edges.sort(key = lambda x : int(x[2])) #linija iz helpa
   
    for i in range(len(svePutanje)):
        edge = edges[i]


        grafBridova[edge[0]] = [(edge[1],edge[2])]
    
    print(grafBridova)
    return grafBridova

def konverzijaGrafUListu(graf): # koristi se u funkciji sortiranje bridova
    listaBridova = []

    for i in graf:
        for j in sorted(graf[i].items(), key = lambda kv:(int(kv[1]), kv[0])):

            safeToAdd = True
            for n in range(len(listaBridova)): #prolazim svaki niz u nizu i provjeravam jeli postoji 
                if j[1] in listaBridova[n]:
                    safeToAdd = False
                
            if safeToAdd:
                listaBridova.append((i,j[0],j[1]))
    return listaBridova

def main():

    svePutanje = readCSV()  # citaj i spremi u {grad:{grad:udaljenost}, grad:{grad:udaljenost}}

    start = time.time()
    najkraciPut= bruteForce(svePutanje) #koristija sam manji file radi memory errora
    print(time.time() - start, "sekundi")


    start = time.time()
    najkraciPut= najblizegSusjeda(svePutanje)
    print(time.time() - start, "sekundi")

    
    start = time.time()
    najkraciPut= sortiranihBridova(svePutanje)
    print(time.time() - start, "sekundi")



if __name__=='__main__':
    main()




