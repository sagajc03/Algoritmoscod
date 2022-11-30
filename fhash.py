# Valencia Vazquez Javier
# Vazquez Rioja Jesus Alberto
# Salas Gallegos Juan Carlos

def encode(key):
    key += 50
    return key

def decode(key):
    key -= 50
    return key

llaves = [1132,2011,1111,2000,2014,1101,2009,1100,1105,1133]
for i in range(0,len(llaves)):
    llaves[i] = encode(llaves[i])
print(llaves)
for i in range(0,len(llaves)):
    llaves[i] = decode(llaves[i])
print(llaves)