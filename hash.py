#Funciones hash, que aparte sirven para encrptar

#Numeros a buscar
def encripta(valor,vector):
    letras = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    letra = ['a','b','c','d','e','f','g''h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vector_aux = []
    aux = str(valor)
    for i in range(len(aux)):
        vector_aux.append(aux.split(''))
    for i in range(len(vector_aux)):
        for j in letra:
            if j == vector_aux[i]:
                vector_aux[i] = letras[j]

def encode(word):
    SUM = 0
    for char in word:
        value = ord(char)
        SUM += value
    SUM += 3
    return SUM

def decode(SUM):
    SUM = 0

valor = 'alo'
vector = []
# encripta(valor,vector)

word = 'COMPUTER'
SUM = 0
for char in word:
    value = ord(char)
    SUM += value

print(SUM)
    
     
