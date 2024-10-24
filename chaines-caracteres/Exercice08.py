# Exercice 8
def ipValid(ip:str) ->bool:
    # ip : A.B.C.D
    L = list(map(lambda e : int(e),ip.split(".")))
    if len(L) != 4 :
        return False
    for e in L:
        if not e.isdigit():
            return False
        e = int(e)
        if e<0 or e>255:
            return False
    return True

print(ipValid("192.168.265.8"))