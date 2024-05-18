# GGT algorithm

zahl1 = int(input("gibt den ersten Zahl ein: "))
zahl2 = int(input("gibt den zweiten zahl ein: "))

while zahl2 != 0:
    temp = zahl2
    zahl2 = zahl1 % zahl2
    a = temp

print(f"Der GGT von {zahl1,zahl2} ist {a}")