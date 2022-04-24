from hashlib import sha256
import random

alfanum="abcdefghijklmnopqrstuvwxyz1234567890"
comparador=False
cadena="a"
while(comparador==False):
    cont=random.randint(0,len(alfanum)-1)
    cadena=cadena+alfanum[cont]
    hash_actual=sha256(cadena.encode()).hexdigest()
    if(hash_actual.find("b00da")!=-1):
        print(cadena)
        print(hash_actual)
        comparador=True

