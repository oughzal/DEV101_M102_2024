
n = int(input("Donner le numerateur n : "))
d = int(input("Donner le denominateur d : "))
if n < d :
    i = n
else :
    i = d
i = d if n <d else d # i = (n<d)? n : d
while n % i != 0 or d % i != 0 :
    i = i-1
if d / i == 1 :
    print(n,"/",d,"=",n / i )
else :
    print(n,"/",d,"=",n / i ,"/",d / i)