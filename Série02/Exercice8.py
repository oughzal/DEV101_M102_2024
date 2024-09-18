a=int(input("donner la valeur de a:"))
b=int(input("donner la valeur de b:"))
if a<0:
    if b<0:
        print("négatif")
    else: # a<0 et b>0
        if b> -a:
            print("positif")
        else: # a<0 et b>0 et b<-a
            print("négatif")
else:# a>0
    if b>0:
        print("positif")
    else: # a>0 et b<0
        if a> -b:
            print("positif")
        else:
            print("négatif")
