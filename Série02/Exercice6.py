from math import sqrt
a = float(input("Donner a : "))
b = float(input("Donner b : "))
c = float(input("Donner c : "))
d = b**2 - 4*a*c
if d<0:
    print("Pas de solutions dans R")
elif d==0:
    x1 = -b/(2*a)
    print(f"une seule solution x={x1}")
else:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    print(f"deux solution : x1={x1} et x2={x2}")
