import os

def pravljenjeArhive():
    imeArhive = input("Unesite ime arhive")
    if (os.path.exists(imeArhive)):
        print("Postoji arhiva sa istim imenom")
    else:
        os.mkdir("Arhive/" + imeArhive)
        print("Uspesno ste napravili arhivu")

def pravljenjeZapisnika():
    imeZapisnika = input("Unesite ime zapisnika: ")
    if (os.path.exists(imeZapisnika)):
        print("Postoji zapisnik sa tim imenom")
    else:
        zapisnik = open(imeArhive + "/" + imeZapisnika + ".txt", "w")
        print("Uspesno ste napravili zapisnik")
        zapisnik.close()

if (not os.path.exists("Arhive")):
        os.mkdir("Arhive")

while True:
    print("1. Unos nove arhive\n2. Unos novog zapisnika\n3. Unos sadrzaja u zapisnik\n4. Dodaj sadrzaj u zapisnik"
          "\n5. Izlistaj sve zapisnike\n6. Prikazi zapisnik\n7. Obrisi zapisnik\n8. Izlaz\n")
    opcija = int(input("Unesite opciju:"))
    if opcija==1:
        pravljenjeArhive()
    if opcija==2:
        imeArhive = input("Unesite ime arhive: ")
        if (not os.path.exists("Arhive/"+imeArhive)):
            print("Ne postoji arhiva sa istim imenom")
        else:
            pravljenjeZapisnika()
    if opcija==3:
        imeZapisnika = input("Unesite ime zapisnika: ")
        if (not os.path.exists("Arhive/"+imeZapisnika)):
            print("Ne postoji zapisnik sa tim imenom")
        else:
            zapisnik = open(imeZapisnika + ".txt", "w")
            zapisnik.write(input("Unesite tekst koji zelite da upisete: "))
            print("Tekst je uspesno sacuvan.")
            zapisnik.close()
    if opcija==4:
        imeZapisnika = input("Unesite ime zapisnika: ")
        if (not os.path.exists("Arhive/" + imeZapisnika)):
            print("Ne postoji zapisnik sa tim imenom")
        else:
            zapisnik = open(imeZapisnika + ".txt", "a")
            zapisnik.write(input("Unesite tekst koji zelite da upisete: "))
            print("Tekst je uspesno sacuvan.")
            zapisnik.close()
    if opcija==5:

    if opcija==8:
        print("Napustate aplikaciju")
        break