T = float(input("Donner la température : "))
if T <= 0 :
    print("Solide")
elif T <=100 :
    print("Liquide")
else:
    print("Gaz")