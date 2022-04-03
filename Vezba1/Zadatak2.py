import random

def sifruj(poruka):
    sifrovana = ''

    for i in poruka:
        sifrovana += recnik[i]

    return sifrovana

def desifruj(poruka):
    desifrovana = ''
    obrnutiKljucVrednostRecnik = dict((v, k) for k, v in recnik.items())    #Obrce kljuc vrednost (vrednost postaje kljuc, kljuc postaje vrednost)

    for i in poruka:
        desifrovana += obrnutiKljucVrednostRecnik[i]

    return desifrovana

recnik = {}
iskoriscena = []

for i in range(65, 91):
    vrednost = chr(random.randrange(65, 91))

    while iskoriscena.__contains__(vrednost):
        vrednost = chr(random.randrange(65, 91))

    recnik.update({chr(i): vrednost})

    iskoriscena.append(vrednost)

print(recnik)

sifrovana = sifruj('PORUKA')

print('Sifrovana poruka je ' + sifrovana)

desifrovana = desifruj(sifrovana)

print('Desifrovana poruka je ' + desifrovana)