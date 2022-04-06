#Zadatak1

import math
import random

def f(x):
    return x**2

def g(x):
    return math.sqrt(x)

N = 100000
brojac = 0

for i in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if y < g(x) and y > f(x): #Ispod i iznad
        brojac += 1

print('Povrsina je ' + str(brojac/N))


#Zadatak2
rec = 'N^MZC'

for i in range(5, 15):
    pomRec = ''
    for j in rec:
        pomRec += chr(ord(j) ^ i)
    print(pomRec)

#Zadatak3

import os
import time

red = 0
kolona = 0

smer = 1

while True:
    for i in range(20):
        for j in range(20):
            c = ''
            if j == 19:
                c = '\n'

            if i == red:
                print('@', end=c)
            else:
                if j == kolona:
                    print('@', end=c)
                else:
                    print(' ', end=c)

    if red >= 19 and kolona >= 19:
        smer = -1
    elif red <= 0 and kolona <= 0:
        smer = 1

    red += smer
    kolona += smer

    time.sleep(.1)
    os.system('cls')