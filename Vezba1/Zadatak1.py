import random

def ispis():
    for i in recLista:
        if i in listaPogodjenihSlova:
            print(i, end="")
        else:
            print("_", end="")

def ispisPromasenih():
    print("Promasena imena:")
    for i in listaPromasenihImena:
        print(i + ",", end="")
    print()
    print("Promasena slova:")
    for i in listaPromasenihSlova:
        print(i + ",", end="")
    print()

brojac=0
lista=["Igor","Lana","Steva","Filip"]
listaPromasenihSlova=[]
listaPogodjenihSlova=[]
listaPromasenihImena=[]
rec = random.choice(lista)
rec=rec.lower()
str=""
for i in rec:
    str+="_"
recLista=list(rec)
print("Zadato ime je: "+str)
while brojac<len(rec):
    opcija=input("1. Unesi ime\n2. Unesi slovo\n3. Izlaz\n")
    postoji = False
    if len(opcija)>1 or (not opcija.isdigit()) or int(opcija)>3:
        print("Opcija mora biti iz liste.")
    else:
        opcija=int(opcija)
    if opcija==1:
        unos = input("Unesite ime\n")
        for i in listaPromasenihImena:
            if unos==i:
                postoji=True
        if len(unos)<3:
            print("Ime ne moze biti krace od 3 slova.")
        elif postoji==True:
            print("Vec ste uneli ime "+unos)
        elif unos.lower()==rec:
            print("POGODILI STE REC.\nIgra je zavrsena.")
            break
        else:
            listaPromasenihImena.append(unos)
            brojac+=1
        ispis()
        print()
        ispisPromasenih()
    elif opcija==2:
        unos = input("Unesite slovo \n")
        for i in listaPromasenihSlova:
            if unos==i:
                print("Vec ste uneli slovo "+unos)
        else:
            for i in range(len(recLista)):
                if unos==recLista[i]:
                    listaPogodjenihSlova.append(unos)
                    postoji=True
            if postoji==False:
                listaPromasenihSlova.append(unos)
                brojac+=1
        ispis()
        print()
        ispisPromasenih()
    elif opcija==3:
        print("Program se zatvara.")
        break
    if len(listaPogodjenihSlova)==len(recLista):
        print("Uspesno ste pogodili ime.")
        break
if brojac==5:
    print("Niste pogodili ime.")
    print("Zadato ime je "+rec)