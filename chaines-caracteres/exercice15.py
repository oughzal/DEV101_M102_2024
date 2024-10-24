#Exercice 15
def charUniq(s:str)->bool:
    # return not any([e for e in s if s.count(e)>1])
    for c in s:
        if s.count(c)> 1:
            return False
    return True
print(charUniq("abc"))
