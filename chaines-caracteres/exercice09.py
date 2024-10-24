# Exercice 9
def isPalindrom(s:str)->bool:
    # return s == s[::-1]
    i = 0
    j = len(s) - 1
    while i < j :
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print(isPalindrom("LAVAL"))