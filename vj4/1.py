def readFile():
    #Ovdje upisite ime vašeg file-a
    with open("D:/Faks/Metode Optimizacije/vj4/football.net", "r") as f:
        lines = f.readlines()
    
    return lines

def breakApart(string):
    return string.split()

def splitCategories(lines,allCategories):    
    temp = []    

    changeOccured = False
    firstItteration = True

    for line in lines:
        line = breakApart(line)

        if("*" in line[0]):
            changeOccured = True
            if(firstItteration):
                changeOccured = False
                firstItteration = False
            

        if(changeOccured):
            allCategories.append(temp)
            temp = []
            changeOccured = False

        
        temp.append(line)
        
    allCategories.append(temp)

    return allCategories       


def adjacencyList():
    weighted = False
    directed = False

    allLines = readFile()

    adjacencyList = {}
    allCategories = []
    allCategories = splitCategories(allLines,allCategories)

    if(len(allCategories[1]) > 1):
        directed = True


    if(directed == False and len(allCategories[2][1]) == 3):
        weighted = True
    elif(directed == True and len(allCategories[1][1]) == 3):
        weighted = True

    temp = []

    tempWeighted = []
     
    if(directed):
        arcs = allCategories[1]
        for x in range(1, len(allCategories[0])):       
            if allCategories[0][x][0] not in adjacencyList:   
                adjacencyList[allCategories[0][x][0]] = []

        
        #Kod eva se dogadao problem gdje bi KeyError: '2321'
        for x in range(1, len(arcs)): 
            if arcs[x][1] not in adjacencyList:
                adjacencyList[arcs[x][1]] = []
        

            

        if(weighted):
            for x in range(1, len(arcs)):
                tempWeighted = []
                temp = adjacencyList[arcs[x][0]]

                if(arcs[x][1] not in temp): #provjera ako ima duplikata
                    tempWeighted.append(arcs[x][1])
                    tempWeighted.append(arcs[x][2])

                    temp.append(tempWeighted)
                    temp.sort(key=lambda x:x[0])   

                    adjacencyList[arcs[x][0]] = temp


                #Ako se ovo ostavi onda se gubi smjer
                """
                #kako bih nadodali drugi vertice
                tempWeighted = []
                temp = adjacencyList[arcs[x][1]]

                if(arcs[x][0] not in temp): #provjera ako ima duplikata
                    tempWeighted.append(arcs[x][0])
                    tempWeighted.append(arcs[x][2])

                    temp.append(tempWeighted)
                    temp.sort(key=lambda x:x[0])   

                    adjacencyList[arcs[x][1]] = temp    
                """

        else:
            for x in range(1, len(arcs)):
                temp = adjacencyList[arcs[x][0]]

                if(arcs[x][1] not in temp): #provjera ako ima duplikata
                    temp.append(arcs[x][1]) 
                    temp.sort()  

                    adjacencyList[arcs[x][0]] = temp
                

                """
                temp = adjacencyList[arcs[x][1]]

                #kako bih nadodali drugi vertice
                if(arcs[x][0] not in temp): #provjera ako ima duplikata
                    temp.append(arcs[x][0])   
                    temp.sort()

                    adjacencyList[arcs[x][1]] = temp
                """

                   
    else:
        edges = allCategories[2]

        for x in range(1, len(allCategories[0])):       
            if allCategories[0][x][0] not in adjacencyList:   
                adjacencyList[allCategories[0][x][0]] = []

    
        for x in range(1, len(edges)): 
            if edges[x][1] not in adjacencyList:
                adjacencyList[edges[x][1]] = []


        if(weighted):
            for x in range(1, len(edges)):
                tempWeighted = []
                temp = adjacencyList[edges[x][0]]

                if(edges[x][1] not in temp): #provjera ako ima duplikata
                    tempWeighted.append(edges[x][1])
                    tempWeighted.append(edges[x][2])

                    temp.append(tempWeighted)
                    temp.sort(key=lambda x:x[0])   

                    adjacencyList[edges[x][0]] = temp


                #kako bih nadodali drugi vertice
                tempWeighted = []
                temp = adjacencyList[edges[x][1]]

                if(edges[x][0] not in temp): #provjera ako ima duplikata
                    tempWeighted.append(edges[x][0])
                    tempWeighted.append(edges[x][2])

                    temp.append(tempWeighted)
                    temp.sort(key=lambda x:x[0])   

                    adjacencyList[edges[x][1]] = temp  
        else:  
            for x in range(1, len(edges)):
                temp = adjacencyList[edges[x][0]]

                if(edges[x][1] not in temp): #provjera ako ima duplikata
                    temp.append(edges[x][1]) 
                    temp.sort()  

                    adjacencyList[edges[x][0]] = temp
                
                temp = adjacencyList[edges[x][1]]

                #kako bih nadodali drugi vertice
                if(edges[x][0] not in temp): #provjera ako ima duplikata
                    temp.append(edges[x][0])   
                    temp.sort()

                    adjacencyList[edges[x][1]] = temp



    
    return [directed,weighted,adjacencyList]


adjecencyInfo = adjacencyList()

print("The adjecency list is directed: ",adjecencyInfo[0])
print("The adjecency list is Weighted: ",adjecencyInfo[1])
print("The adjecency list: ", adjecencyInfo[2])
