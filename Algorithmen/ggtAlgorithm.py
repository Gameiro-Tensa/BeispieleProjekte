# GGT Algorithm mit einer Funktion implementiert

def ggt(a, b):
    while b != 0:
        #a, b = b, a % b
        a = b
        b = a % b
    return a

zahl1 = int(input("geben Sie den ersten zahl ein: "))
zahl2 = int(input("geben Sie den zweiten zahl ein: "))

ergebnis = ggt(zahl1, zahl2)

print(f"Der GGT von {zahl1,zahl2} ist {ergebnis} ")