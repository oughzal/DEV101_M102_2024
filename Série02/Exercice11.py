A = int(input("Donner l'année : "))
if A % 400==0 or (A % 4 == 0 and A % 100 != 0):
    print(f"{A} est une anné bissextile")
else:
    print(f"{A} n'est pas une anné bissextile")