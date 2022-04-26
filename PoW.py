from hashlib import sha256
import random

comparador=False
n=0
cadena=": ¡Hola_mundo!"
while(comparador==False):
    for i in range(33,127):
        cadena_aux=chr(i)+cadena
        hash_actual=sha256(cadena.encode()).hexdigest()
        if(hash_actual.find("b00da")!=-1):
            print(cadena)
            print(hash_actual)
            n=1
        break
    if(n==1):
        comparador=True   
    else:
        cadena=chr(random.randint(33,126))+cadena

