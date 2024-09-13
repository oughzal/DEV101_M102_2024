c = input("donner un caractère : ")

if c >='a' and c <='z' :
    print(c, " est une miniscule")
elif c >='A' and c <='Z' :
    print(c, " est une majuscule")
elif c >='0' and c <='9':
    print(c, " est un chiffre")
else:
    print(c, " est un symbole")
