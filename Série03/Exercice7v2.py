N = int(input("Donner un nombre : "))
i= 2
while  i<N and N % i != 0 :
 i = i+ 1
if i == N :
   print (N, " est premier")
else :
   print(N, " n'est pas premier")
