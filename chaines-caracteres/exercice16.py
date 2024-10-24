# exercice 16
def isAlpha(s:str)->bool:
    # return not any([c for c in s if not c.isalpha()])
    for c in s:
        if not c.isalpha():
            return False
    return True
print(isAlpha("aBcDé"))

