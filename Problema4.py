#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).
a=int(input('a='))
b=int(input('b='))
for i in range(a,b):
    if i%2==1:
        print(i)