def T_Sort(Q,gradoEntrada,E):
    ST = [] 
    while (len(Q) != 0 ): 
        T = Q.pop(0) #saco el elemento en la primera posicion pq trabajo con colas (FIFO)
        ST.append(T)
        for vecino in E[T]: 
            gradoEntrada[vecino] -=1
            if gradoEntrada[vecino] == 0: 
                Q.append(vecino)

    if len(ST) == len(E): 
        return ST 
    return "Hay ciclo"

def funcion_auxiliar(Q,gradoEntrada,E): 
    for nodo in E: #recorro el grafo y en el diccionario guardo cuantos grados de entrada tiene 
            gradoEntrada[nodo] = 0
    
    for nodo in E: 
        for vecino in E[nodo]: 
            gradoEntrada[vecino] +=1
    #meto todos los minimales a Q
    for nodo in gradoEntrada: 
        if gradoEntrada[nodo] == 0: 
            Q.append(nodo)



def main(): 
    E = {
        "Algebra":     {"AnalisisI"}, # apunta a AnalisisI
        "AnalisisI":   {"AnalisisII", "Fisica"},
        "AnalisisII":  set(),
        "Fisica":      {"Termo"},
        "Termo":       set(),
    }

    Q=[]
    gradoEntrada = {}

    funcion_auxiliar(Q,gradoEntrada,E)
    print("T-SORT: ",T_Sort(Q,gradoEntrada,E))

    E2 = {"A": {"B"}, "B": {"C"}, "C": {"A"}}
    Q2 = [] 
    gradoEntrada2 = {}
    funcion_auxiliar(Q2,gradoEntrada2,E2)
    print("T-SORT: ",T_Sort(Q2,gradoEntrada2,E2))
    
main()

    

