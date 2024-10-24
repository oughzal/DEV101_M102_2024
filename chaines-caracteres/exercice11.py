# Exercice 11
def wordCount(s:str)->int:
    # return len(s.split())
    if s=="":
        return 0
    nb = 1
    for c in s :
        if c == " ":
            nb +=1
    return nb

print(wordCount("DEV 101"))