def sin_repetidos(lista):
    resultado = []
    for i in range (0, len(lista)):
        if lista[i] not in resultado:
            resultado[i:] = lista[i]
    print(resultado)
    
sin_repetidos(['q','w','a','d','f','d','w','a','f','f','z','q','j'])    