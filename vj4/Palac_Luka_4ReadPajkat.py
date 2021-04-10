import random
from collections import deque 

def cistenjeStringa(string):
    badChars = ['"',',','\n']
    for i in badChars:
        string = string.replace(i, '')
    return string

def readPajkat(): # Vraca nam Verticels , Arcs , Edges
    brojacKategorija = 0 #Verticels = 1, Arcs = 2, Edges = 3. 
    verticels = []
    arcs = []
    edges = []
    temp=[]
    listaSusjeda={}
    
    with open("D:/Faks/Metode Optimizacije/vj4/euler.net", "r") as inputfile:
        for line in inputfile:
            line=cistenjeStringa(line)


            if("*" in line): #Dize broj 
                brojacKategorija += 1 

            elif brojacKategorija == 1:#Verticels = 1
                verticels.append(line.split())
            elif brojacKategorija == 2:#Arcs = 2
                arcs.append(line.split())
            elif brojacKategorija == 3:#Edges = 3
                edges.append(line.split())
                
    #print ("Verticals su: ",verticels)
    #print ("Arcs su: ",arcs)
    #print ("Edges su: ",edges)
    return verticels,arcs,edges 

def provjeraVrsteGrafa(arcs,edges): #graf moze bili ili usmjereni ili težinski
    usmjeren = False
    tezina = False
    arcsFlag = False
    edgesFlag = False

    if len(arcs) > 1: # ako postoji ista unutra
        arcsFlag = True
        usmjeren = True
        if len(arcs[0]) > 2 : # ako postoji treca znamenka u arcu 
            tezina = True
    else:  
        print("Nepostoje Arcovi") 

    if len(edges) != 0:
        edgesFlag = True
        if len(edges[0]) > 2 : # ako postoji treca znamenka u edgeu
            tezina = True
    else:
        print("Nepostoje Edgevi")

    #ispis
    if usmjeren:
        print ("Graf je usmjeren")
    else:
        print ("Graf nije usmjeren")
    if tezina:
        print ("Graf je tezinski")
    else:
        print("Graf nije tezinski")
    
    return arcsFlag, edgesFlag, usmjeren, tezina

def makeListuSusjedstva():
    listaSusjedstva= dict()
    tempSort = []

    verticals,arcs,edges = readPajkat()

    arcsFlag, edgesFlag,usmjeren,tezina = provjeraVrsteGrafa(arcs,edges) #provjeravanje flagova
    
    if arcsFlag:
        for x in range(len(verticals)):
            for red in arcs:
                if tezina: # ako je tezinski nece dodavat samo ime nego i broj tezine
                    if red[0] in verticals[x][0]:
                        ime = numInStringArray(red[1],verticals) #change numbers to string
                        imeTezina = [ime,red[2]]
                        tempSort.append(imeTezina) #dodaje broj i tezinu s kojim se povezuje

                    if not usmjeren:  # nece ici u drugom smjeru jer je usmjeren
                        if red[1] in verticals[x][0]: 
                            ime = numInStringArray(red[0],verticals) 
                            imeTezina = [ime,red[2]]
                            tempSort.append(imeTezina)
                else:
                    if red[0] in verticals[x][0]:
                        ime = numInStringArray(red[1],verticals) #change numbers to string
                        tempSort.append(ime) #dodaje broj s kojim se povezuje

                    if not usmjeren:  # nece ici u drugom smjeru jer je usmjeren
                        if red[1] in verticals[x][0]: 
                            ime = numInStringArray(red[0],verticals) 
                            tempSort.append(ime)

            listaSusjedstva[verticals[x][1]] = tempSort
            tempSort = []

    if edgesFlag:
        for x in range(len(verticals)):
            for red in edges:
                if tezina: # ako je tezinski nece dodavat samo ime nego i broj tezine
                    if red[0] in verticals[x][0]:
                        ime = numInStringArray(red[1],verticals) #change numbers to string
                        imeTezina = [ime,red[2]]
                        tempSort.append(imeTezina) #dodaje broj i tezinu s kojim se povezuje

                     # nece ici u drugom smjeru jer je usmjeren
                    if red[1] in verticals[x][0]: 
                        ime = numInStringArray(red[0],verticals) 
                        imeTezina = [ime,red[2]]
                        tempSort.append(imeTezina)
                else: 
                    if red[0] in verticals[x][0]:
                        ime = numInStringArray(red[1],verticals) #change numbers to string
                        tempSort.append(ime) #dodaje broj s kojim se povezuje

                    elif red[1] in verticals[x][0]: 
                        ime = numInStringArray(red[0],verticals) 
                        tempSort.append(ime)

            listaSusjedstva[verticals[x][1]] = tempSort
            tempSort = []

    #ispis
    print ("ovo je graph liste susjeda")
    for i in verticals:
        print(i[1]," - ", listaSusjedstva[i[1]])
    
    return listaSusjedstva

def numInStringArray(num,verticals): #nije bas najbolje optimiziran ali ako zelimo lijep ispis radimo ovu funkciju 
    string = ""
    for i in range(len(verticals)):
        if num == verticals[i][0]:
            string = verticals[i][1]
            break
    return string

def makeMatricaIndicije(listaSusjeda):
    matricaIndicije=[]
    verticals = list()
    #dobivanje nit verticala iz liste susjeda
    for i in listaSusjeda.keys():
        verticals.append(i)
        
    
    edges = brojBridova(listaSusjeda)
       
    for i in range(len(listaSusjeda)):
        matricaIndicije.append([])
        for j in range(edges):
            
            matricaIndicije[i].append(0)


    #nazalost nemogu smislit nacin kako da stupce ili edgeve skupim dobrim redosljedom pa da mogu ih stavit u tablicu pa sam moramo read filat
    #ucitane varijable sa fila imaju veliko pocetno slovo
    Vertocals,Arcs,Edges=readPajkat()
    ArcsFlag, EdgesFlag,Usmjeren,Tezina = provjeraVrsteGrafa(Arcs,Edges) #provjeravanje flagova
    stupac = 0
    if Usmjeren:
        if Tezina:
            for i in listaSusjeda:
                for j in Arcs:
                    if stupac >edges-1:
                        break
                    red1 = int(j[0]) - 1
                    red2 = int(j[1]) - 1
                    matricaIndicije[red1][stupac] = int(j[2])
                    matricaIndicije[red2][stupac] = int(j[2])
                    stupac +=1 
        else:
            for i in listaSusjeda:
                for j in Arcs:
                    if stupac >edges-1:
                        break
                    red1 = int(j[0]) - 1
                    red2 = int(j[1]) - 1
                    matricaIndicije[red1][stupac] = 1
                    matricaIndicije[red2][stupac] = 1
                    stupac +=1 
    else:
        if Tezina:
            for i in listaSusjeda:
                for j in Edges:
                    if stupac >edges-1:
                        break
                    red1 = int(j[0]) - 1
                    red2 = int(j[1]) - 1
                    matricaIndicije[red1][stupac] = 1
                    matricaIndicije[red2][stupac] = 1
                    stupac +=1 
        else:
            for i in listaSusjeda:
                for j in Edges:
                    if stupac > edges-1:
                        break
                    red1 = int(j[0]) - 1
                    red2 = int(j[1]) - 1
                    matricaIndicije[red1][stupac] = 1
                    matricaIndicije[red2][stupac] = 1
                    stupac +=1
    print ("\n Ovo je matrica indicije")
    for i in range(len(matricaIndicije)):
        print (matricaIndicije[i])
    return matricaIndicije

def makeMatricaSusjedstva(listaSusjeda):
    matricaSusjedstva=[]
    verticals = list()
    tezina = False
    #dobivanje nit verticala iz liste susjeda
    for i in listaSusjeda.keys():
        verticals.append(i)

    #init
    for i in range(len(listaSusjeda)):
        matricaSusjedstva.append([])
        for j in range(len(listaSusjeda)):
            matricaSusjedstva[i].append(0)

    # trazenje jeli graf tezinski
    try:  
        for i in listaSusjeda:
            for j in listaSusjeda[i]:
                if j[0] in verticals:
                    stupac=verticals.index(i)
                    red = verticals.index(j[0])
                    matricaSusjedstva[stupac][red] = j[1]

    except:
        for i in listaSusjeda:
             for j in listaSusjeda[i]:
                if j in verticals:
                    stupac=verticals.index(i)
                    red = verticals.index(j)
                    matricaSusjedstva[stupac][red] = 1
            
    #znan da je los naci ovo trazejne ali potrosija sam previse vrimena na type i isinstance i dolazenje do nje ovo je jedino sto je radilo
    

    print ("\n Ovo je matrica susjedstva")
    for i in range(len(matricaSusjedstva)):
        print (matricaSusjedstva[i])
    return matricaSusjedstva


def nadiBrojVrhova(listaSusjeda): #3.1 zadatak
    brojac=0
    for i in listaSusjeda.keys():
        brojac += 1

    return brojac

def nadiBrojBridova (listaSusjeda): #3.2 zadatak
    edges = 0
    for i in listaSusjeda:
        for j in listaSusjeda[i]:
            edges +=1
    return int(edges / 2) 

def nadiBrojStupnjaVrhova (listaSusjeda):#3.3 zadatak
    stupanj = {}
    brojacStupnjeva = 0
    for i in listaSusjeda:
        for j in listaSusjeda[i]:
            brojacStupnjeva += 1
        stupanj[i]=brojacStupnjeva
        brojacStupnjeva = 0
    return stupanj
        
 
def nadiMaxBrojIncBridova(listaSusjeda):#3.4 zadatak
    maksimalni = 0
    maxName = []
    for i in listaSusjeda:
        
        if len(listaSusjeda[i])>maksimalni:
            maksimalni = len(listaSusjeda[i])
            maxName = []
        if len(listaSusjeda[i]) == maksimalni:
            maxName.append(i)
    print ("Najduži je vrh ", maxName, "sa duljinom ", maksimalni)
    return maxName

def euler(listaSusjeda):

    usmjereni=False

    start = random.choice(list(listaSusjeda.keys())) #random start

    brojBridova = nadiBrojBridova(listaSusjeda) 
    brojIzlaza = nadiBrojStupnjaVrhova(listaSusjeda)

    putanja = traziPut(start,brojIzlaza,listaSusjeda)

    print (putanja)

    if usmjereni:
        if len(putanja)== brojBridova+1:
            return putanja
        else:
            print("Nije našlo eulerov put")
            return None
    else: #nije usmjeren
        if len(putanja)==(brojBridova*2)+1: #*2 zato sto ce napravit 2 crte na svakom bridu
            return putanja
        else: 
            print("Nije našlo eulerov put")
            return None

def traziPut(trenutni,brojIzlaza,listaSusjeda):
        putanja = []
        iduci = {}
        while(brojIzlaza[trenutni]!=0): #dok zadni(prvi) element nema 0 edgeva
            
            iduci = randomSusjed(trenutni,listaSusjeda)
            brojIzlaza[trenutni] -= 1 
            listaSusjeda[trenutni].remove(iduci) # mozda bi bilo bolje da removan sa nekim if on bi bi onda uvijek nalazio put?
            putanja = traziPut(iduci,brojIzlaza,listaSusjeda)
            

        putanja[:0]=[trenutni] 
        return putanja

def randomSusjed(trenutni,listaSusjeda):
    sljedeci = random.choice(list(listaSusjeda[trenutni])) #random value iz odredenog keya
    return sljedeci

listaSusjeda = makeListuSusjedstva()# 1 zadataka 

#makeMatricaIndicije(listaSusjeda) #2 zadatak 
#makeMatricaSusjedstva(listaSusjeda) #2 zadatak

#3 zadatak
#nadiBrojVrhova(listaSusjeda) 
#nadiBrojBridova(listaSusjeda)
#nadiBrojStupnjaVrhova(listaSusjeda)
#nadiMaxBrojIncBridova(listaSusjeda)

#4 zadatak samo sa euler file jer nisam radi sa tezinama. ali radi sa usmjerenim ili ne usmjerenim 2/3 sansa da ne nade cini mi se tako iz mog testiranja
euler(listaSusjeda)
