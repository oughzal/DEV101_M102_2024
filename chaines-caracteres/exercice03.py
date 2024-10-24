# Exercice 3
def isDigit(ch:str)->bool :
    # return ch.isdigit()
    for c in ch:
        if c <'0' or c>'9':
            return False
    return True

print(isDigit("123"))