import time
import calendar
import os

print(time.time())

print(time.localtime(time.time()))
print(time.gmtime())

print(time.strftime("%d.%m.%Y %H:%M:%S"))

#time.sleep(1)
#print("Pauza od sekund")

print(calendar.calendar(2022))

if(not os.path.exists("zapisnici")):
    os.mkdir("zapisnici")

f=open("zapisnici/a1.txt","a")
f.write("Prva linija\nDruga linija\nTreca linija\n")
f.close()

f2=open("zapisnici/a1.txt","r")
#print(f2.tell())
#f2.seek(5,0)
#sadrzaj=f2.read()
sadrzaj=f2.readline()
print(sadrzaj)
f2.close()

if(os.path.isfile("zapisnici/a1.txt")):
    print("Tacno")

if(os.path.isdir("zapisnici")):
    print("Tacno")

print(os.listdir("zapisnici"))

#os.remove("zapisnici/a1.txt")