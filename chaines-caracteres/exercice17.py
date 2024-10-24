# Exercice 17
def etoiles(s : str)-> str:
    # return "*".join(list(s))
    result = ""
    for c in s:
        result += c + "*"
    return result[:-1] 
print(etoiles("DEV101"))
print(f"DEV101")
