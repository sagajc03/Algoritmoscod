import numpy as np
#Busqueda Lineal
# Valencia Vazquez Javier
# Vazquez Rioja Jesus Alberto
# Salas Gallegos Juan Carlos


def buslineal(vector,valorBuscado):
    for i in range(0,len(vector)):
        print("aaaaaaa")
        if vector[i] == valorBuscado:
            
            cadena = "El valor " + str(valorBuscado) + " se encontro en la posicion " + str(i)
            print(vector[i])
            return cadena
    cadena = "No se encontro"
    return cadena

# a = np.random.randint(10000000,size=1000000)
# print(a)
a = [63, 94, 111, 125, 204, 209, 250, 290, 310, 348, 420]
n = int(input("Que numero quieres buscar? "))
print(buslineal(a,n))
