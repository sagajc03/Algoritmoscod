import numpy as np
from time import time
#Codigo de ordenamiento por incersion

#Javier Valencia Vásquez
#Jesús Alberto Vásquez Rioja
#Juan Carlos Salas Gallegos
from random import randint

def ordenamiento(vector):
    n = len(vector)
    for j in range(1,n):
        pivote = vector[j]
        i = j - 1
        while i >= 0 and vector[i]>pivote:
            vector[i+1] = vector[i]
            i = i - 1
        vector[i+1] = pivote
    return vector

# a = np.random.randint(10000,size=1000)
# a = [22,33,60,8,2,9,1,10,99,15,12,7,3,50,61,45,65,23,44,59,75,41,24,55,77,88,100,11,0,17]
a = [22,33,60,8,2,9,1,10,99]
print (a)
t0 = time()
a = ordenamiento(a)
print (a)
t1 = time()
print("Tiempo: {0:f} segundos", format (t1-t0))