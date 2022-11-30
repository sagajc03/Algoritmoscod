from time import time

import numpy as np

 #Algoritmo de ordenamiento Shell
  
def shellsort(vectorshell):
    
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Shell Sort"""    
    largo = 0
    
    for i in vectorshell:
        largo += 1
    
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                
                j -= distancia
            vectorshell[j] = val
            print(vectorshell)
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo
    return vectorshell

a = [5,3,2,1,4]
# a = [22,33,60,8,2,9,1,10,99,15,12,7,3,50,61,45,65,23,44,59,75,41,24,55,77,88,100,11,0,17]
print(a)
t0 = time()
a = shellsort(a)
print (a)
t1 = time()
print("Tiempo: {0:f} segundos", format (t1-t0))