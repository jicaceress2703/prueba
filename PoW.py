from hashlib import sha256
import random

comparador=False
n=0
cadena=": ¡Hello World!"
while(comparador==False):
    for i in range(33,127):#En este ciclo se generan los caracteres a partir de su codigo ASCII
        cadena_aux=chr(i)+cadena
        hash_actual=sha256(cadena.encode()).hexdigest()#se crea el hash en hexadecimal
        if(hash_actual.find("b00da")!=-1):
            print(cadena)
            print(hash_actual)
            print(len(cadena))
            n=1
        break
    if(n==1):
        comparador=True  #condicion de frenado del ciclo
    else:
        cadena=chr(random.randint(33,126))+cadena #se le agrega un valor aleatorio a la cadena y se vuelve a empezar

