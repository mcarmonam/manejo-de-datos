def es_igual(lista1,lista2):
    for i in range (0,len(lista1)):
        if(lista1[i] != lista2[i]):      
            return False
    return True    

def es_circular(lista1,lista2):
    contador = 0
    if len(lista1) == len(lista2):
        for i in range (0,len(lista1)):
            lista1.append(lista1[0])
            lista1.pop(0)
            if(es_igual(lista1,lista2)):
                contador += 1
            else:
                contador += 0  
        if (contador == 1):        
            return True
        else:
            return False            
    else:
        return False            

            
l1 = [10,10,0,0,10]
l2 = [10,10,10,0,0]
print(es_circular(l2,l1))          
