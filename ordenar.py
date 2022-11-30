import numpy as np
from time import time
def ordenar(vector):
    for c in range(0,len(vector)):
        pivote=c
        for i in range(c,len(vector)):
            if vector[i] < vector[pivote]:
                aux = vector[i]
                vector[i] = vector[pivote]
                vector[pivote] = aux
        # print(vector)
    return vector


# a = np.random.randint(10000,size=1000)
a = [22,33,60,8,2,9,1,10,99,15,12,7,3,50,61,45,65,23,44,59,75,41,24,55,77,88,100,11,0,17]
print(a)
t0 = time()
a = ordenar(a)
print (a)
t1 = time()
print("Tiempo: {0:f} segundos", format (t1-t0))
# for i in range(1,100):
#     a = [randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100)]
#     print(a)
#     a = ordenar(a)
#     print(a)