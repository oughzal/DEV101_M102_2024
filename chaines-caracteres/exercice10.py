# Exercice 10
from collections import Counter
def charFreq(s:str) ->dict:
    # d = {}
    # for c in set(s):
    #     d[c] = s.count(c)
    # return d
    return dict(Counter(s))

print(charFreq("LAVAL"))
