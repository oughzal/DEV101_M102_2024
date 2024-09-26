n=int(input("donner n: "))
inv=0
print("inverse est ", str(n)[-1::-1])
while n!=0 : 
    inv=inv*10+n%10
    n=n // 10
print("inverse est ", inv)
