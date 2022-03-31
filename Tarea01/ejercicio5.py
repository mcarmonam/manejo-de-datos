
def comprime(cadena):
    letra       = cadena[0]
    apariciones = 1
    cadenaFinal = ''
    for i in range (0, len(cadena)-1):
        if(cadena[i] == cadena[i+1]):
            apariciones += 1
            letra = cadena[i+1]
        else:
            cadenaFinal = cadenaFinal + (str(apariciones) + letra)
            letra = cadena[i+1]
            apariciones = 1
    letra = cadena[i+1]        
    cadenaFinal = cadenaFinal + (str(apariciones) + letra)
    print (cadenaFinal)
    
comprime("aaaabbbbbccccdddx")    