import random as rnd

izbor=["X","O"]
listaIzbora=[]
brojac=0
x,y=0,0

def pravljenjeMatrice():
    for i in range(5):
        lista = []
        for j in range(5):
            lista.append(rnd.choice(izbor))
        listaIzbora.append(lista)

def ispisMatrice():
    global brojac
    brojac=0
    for i in listaIzbora:
        print(''.join(i))
        brojac+=list(i).count("O")

def unosKoordinata(osa):
    global x,y
    unos = input("Unesite "+osa+" koordinatu 1-5:\n")
    while unos.isalpha():
        print("Koordinate ne smeju da sadrze slova!!!")
        unos = input("Unesite "+osa+" koordinatu 1-5:\n")
    if osa=="x":
        x=int(unos)
    else:
        y=int(unos)

pravljenjeMatrice()
ispisMatrice()
while True:
    unosKoordinata("x")
    unosKoordinata("y")

    if not x in range(6) or not y in range(6):
        print("Koordinate moraju biti vece od 0 i manje od 5!!!")
    else:
        x-=1
        y-=1

        for i in range(len(listaIzbora)):
            listaIzbora[i][y]="X"
            for j in range(len(listaIzbora[i])):
                listaIzbora[x][j]="X"
        ispisMatrice()
    print(brojac)
    if brojac==0:
        print("Uspesno ste zavrsili igricu.")
        break