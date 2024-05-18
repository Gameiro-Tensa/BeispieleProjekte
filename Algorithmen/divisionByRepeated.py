# Algorithm Division by repeated substraction
# nber1 ist der Divident und nber2 ist der Divisor

nber1 = int(input("Bitte geben Sie eine Zahl ein, der Divident: "))
nber2 = int(input("Bitte geben die zweite Zahl ein, der Divisor: "))

R = nber1       # R ist der rest
Q = 0           # Q ist der Quotient

while R >= nber2:
    R = R - nber2
    Q = Q + 1

print("\n\nnber1 geteilt durch nber2 ist gleich ")
print("der Quotient Q ist ", Q, "und der Rest R ist ", R)
print(f"der Quotient Q ist {Q} und der Rest R ist {R}")
