import os

def pravljenjeArhive():
    imeArhive = input("Unesite ime arhive:\n")
    if (os.path.exists(imeArhive)):
        print("Postoji arhiva sa istim imenom.")
    else:
        os.mkdir("Arhive/" + imeArhive)
        print("Uspesno ste napravili arhivu.")

def pravljenjeZapisnika():
    imeArhive = input("Unesite ime arhive:\n")
    if (os.path.exists(imeArhive)):
        print("Ne postoji arhiva sa istim imenom.")
    else:
        imeZapisnika = input("Unesite ime zapisnika:\n")
        if (os.path.exists(imeZapisnika)):
            print("Postoji zapisnik sa tim imenom.")
        else:
            zapisnik = open("Arhive/"+imeArhive + "/" + imeZapisnika + ".txt", "w")
            print("Uspesno ste napravili zapisnik.")
            zapisnik.close()

if (not os.path.exists("Arhive")):
        os.mkdir("Arhive")

while True:
    print("1. Unos nove arhive\n2. Unos novog zapisnika\n3. Unos sadrzaja u zapisnik\n4. Dodaj sadrzaj u zapisnik"
          "\n5. Izlistaj sve zapisnike\n6. Prikazi zapisnik\n7. Obrisi zapisnik\n8. Izlaz\n")
    opcija = int(input("Unesite opciju:\n"))
    if opcija==1:
        pravljenjeArhive()
    if opcija==2:
        pravljenjeZapisnika()
    if opcija==3:
        imeZapisnika = input("Unesite ime zapisnika:\n")
        if (not os.path.exists("Arhive/"+imeZapisnika)):
            print("Ne postoji zapisnik sa tim imenom.")
        else:
            zapisnik = open(imeZapisnika + ".txt", "w")
            zapisnik.write(input("Unesite tekst koji zelite da upisete:\n"))
            print("Tekst je uspesno sacuvan.")
            zapisnik.close()
    if opcija==4:
        imeZapisnika = input("Unesite ime zapisnika:\n")
        if (not os.path.exists("Arhive/" + imeZapisnika)):
            print("Ne postoji zapisnik sa tim imenom.")
        else:
            zapisnik = open(imeZapisnika + ".txt", "a")
            zapisnik.write(input("Unesite tekst koji zelite da upisete:\n"))
            print("Tekst je uspesno sacuvan.")
            zapisnik.close()
    if opcija==5:
        listaArhiva=os.listdir("Arhive")
        for i in listaArhiva:
            print("Arhiva: "+i)
            listeZapisnika=os.listdir("Arhive/"+i)
            for j in listeZapisnika:
                print("Zapisnici u arhivi "+i+" su "+j)
    if opcija==6:
        imeArhive = input("Unesite ime arhive:\n")
        if (os.path.exists(imeArhive)):
            print("Ne postoji arhiva sa istim imenom.")
        else:
            imeZapisnika = input("Unesite ime zapisnika: ")
            if (os.path.exists(imeZapisnika)):
                print("Ne postoji zapisnik sa tim imenom.")
            else:
                zapisnik = open("Arhive/" + imeArhive + "/" + imeZapisnika + ".txt", "r")
                sadrzaj=zapisnik.readline()
                print(sadrzaj)
                zapisnik.close()
    if opcija==7:
        imeArhive = input("Unesite ime arhive:\n")
        if (os.path.exists(imeArhive)):
            print("Ne postoji arhiva sa istim imenom.")
        else:
            imeZapisnika = input("Unesite ime zapisnika:\n")
            if (os.path.exists(imeZapisnika)):
                print("Ne postoji zapisnik sa tim imenom.")
            else:
                os.remove("Arhive/"+imeArhive+"/"+imeZapisnika+".txt")
                print("Zapisnik je obrisan.")
    if opcija==8:
        print("Napustate aplikaciju!!!")
        break