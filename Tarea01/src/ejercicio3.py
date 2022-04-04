def invierte_cadena(cadena):
    cadenaInvertida = ""
    for i in cadena:
        cadenaInvertida = i + cadenaInvertida
    return cadenaInvertida

def quita_espacios(cadena):
    cadena_sin_espacios = ''
    for i in cadena:
        if(i != " "):
            cadena_sin_espacios = cadena_sin_espacios + i
    return cadena_sin_espacios                
            
def es_palindromo(cadena):
    aux = quita_espacios((cadena.lower()))
    reversa_cadena = invierte_cadena(aux)
    if aux == reversa_cadena:
        print ("La cadena, " + cadena + ", sí es palindromo")
    else:
        print ("La cadena, " + cadena + ", no es palindromo")

es_palindromo("Lavan esa base naval")

