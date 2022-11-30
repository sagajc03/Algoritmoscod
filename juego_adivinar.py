import random


vector = []
for i in range(0,100):
    vector.append(i)


print(vector)
adivinanza = int(input("Numero: "))
numero = random.randint(0,100)
bandera = False
while bandera == False:
    
    if adivinanza == numero:
        print("Encontrado")
        bandera = True
        break
    if adivinanza > numero:
        if adivinanza > vector[-1]:
            print("Fuera de rango")
        else: 
            print("EL valor es menor a ",adivinanza)
            while vector[-1] != adivinanza:
                # print(vector[-1])
                del vector[-1]
            print(vector)
    if adivinanza < numero:
        if adivinanza < vector[0]:
            print("Fuera de rango")
        else:    
            print("EL valor es mayor a ",adivinanza)
            while vector[0] != adivinanza:
                # print(vector[0])
                del vector[0]
            print(vector)
    adivinanza = int(input("Numero: "))