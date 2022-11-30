# Valencia Vazquez Javier
# Vazquez Rioja Jesus Alberto
# Salas Gallegos Juan Carlos


def buscaTexto(parteTexto, largoParte, texto, largoTexto):
    for i in range(0,largoTexto-largoParte+1):
        j = 1
        while texto[i+j-1] == parteTexto[j-1]:
            j = j + 1
            if j > largoParte:
                return True
    return False


texto = ""
#Abre el archivo de texto en la ubicacion
with open(r"Texto\texto.txt",mode="r") as archivo:
    texto = archivo.read()
    #Guarda el texto del archivo:
    # Hola que se cuenta?
    # Ahhh
    # Bueno
    # ///////////////////////// Texto del archivo original
print(texto)
parte = "Hola"
#parte que se busca
lent = len(texto)
lenp = len(parte)
print(lent,lenp)
print(buscaTexto(parte,lenp,texto,lent))