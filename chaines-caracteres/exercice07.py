def intersection(ch1:str,ch2:str)->list:
    s1 = set(ch1)
    s2 = set(ch2)
    inter =  s1.intersection(s2)
    L =[]
    for c in inter:
        if ch1.count(c)==1 and ch2.count(c)==1:
            L.append(c)
    return L
print(intersection("abcda","eabfgc"))
