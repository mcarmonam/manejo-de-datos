def primera_letra(lista,caracter):
    aux = ''
    indice = 0
    resultado = []
    for i in lista:
        aux = lista[indice]
        primer = aux[0]
        if(primer == caracter):
            resultado.append(lista[indice])
        indice += 1    
    print (resultado)
            
primera_letra(['hola','martin','mario','raton','manzana'],'h')  