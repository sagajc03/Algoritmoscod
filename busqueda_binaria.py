from time import time
global contador


#Busqueda binaria
# Valencia Vazquez Javier
# Vazquez Rioja Jesus Alberto
# Salas Gallegos Juan Carlos
# Costas Rueda Juan Pablo

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


def busquedaB(vector, llave):
    global flag 
    flag = False
    mitad = len(vector)//2
    print(mitad)
    print(vector[mitad])
    if mitad == 0 and not flag:
        return flag
    if vector[mitad] == llave:
        # print("b")
        flag = True
    if vector[mitad] > llave:
        busquedaB(vector[:mitad],llave)
        # print("iz")
    if vector[mitad] < llave:
        busquedaB(vector[mitad:],llave)
        # print("de")
    return flag



vector = [63, 94, 111, 125, 204, 209, 250, 290, 310, 348, 420]
vector = ordenamiento(vector)
print(vector)
llave = 290
t0 = time()
es = busquedaB(vector,llave)
t1 = time()
tiempo = t1- t0
print(es)
print("Tiempo {tiempo} ",format(tiempo))
