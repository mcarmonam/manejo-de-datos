def isPalindrome(cadena):
    aux = (cadena.lower()).replace(" ","")
    reversa_cadena = ''.join(reversed(aux))
    if aux == reversa_cadena:
        print ("La cadena, " + cadena + ", sí es palindromo")
    else:
        print ("La cadena, " + cadena + ", no es palindromo")

isPalindrome("Lavan esa base naval") 