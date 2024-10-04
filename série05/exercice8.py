#exercice8
def estBissextile(A : int) -> bool:
    return  A % 400 == 0 or (A % 4 == 0 and A % 100 != 0)
A = int(input("donner l'année : "))
print(estBissextile(A))