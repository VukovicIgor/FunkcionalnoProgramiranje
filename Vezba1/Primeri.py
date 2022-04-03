import random

print("Pozdrav svete")

a=5
b=5.67
c="Neki tekst"
d=True
a="Tekst"
print(type(a))

a,b,c,=1,56.7,"Tekst"

a,b=b,a

lista=[1,56.7,"Tekst",253]

print(lista)
lista.append("Novi clan")
print(lista)
del(a)
del(lista[0])
print(lista)
lista.remove(253)
print(lista)

lista2=[1,2,3]
lista3=lista+lista2

print(lista3*2)

print(lista3[:4])
print(lista3[3:])
print(lista3[-1])

ntorka=(1,"Tekst",67.8)
print(type(ntorka))
#del(ntorka[0])

recnik={"ime":"Dusan","godiste":1994,2:2500.5}

print(recnik[2])

for i in range(5):
    print(i)
    if i==3:
        print("Pogodak")
    else:
        print("Promasaj")

for i in range(len(lista3)):
    print(lista3[i])

for i in lista3:
    print(i,end="/")

print()
#unos=input("Unesite svoje ime:")
#print(unos)

#random.seed(1)
print(random.random())
print(random.random())

random.shuffle(lista3)
print(lista3)

print(random.choice("Tekst"))

lista=["A","B","C"]

print("".join(lista))