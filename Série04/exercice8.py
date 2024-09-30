T=[1,3,7,9,3,1,9,5,15,2]
# ecrire("donner un entier : ")
n= int(input(" donner l element : "))
nf = 0
for e in T: 
    if n== e : 
        nf = nf + 1
print("ce nombre apparait dans ce tableau ",nf," fois") 
print("ce nombre apparait dans ce tableau ",T.count(n)," fois") 