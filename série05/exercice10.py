#exercice 10
def isPalendrom(s : str) -> bool :
    i = 0
    j = len (s) -1
    while i <= j and s[i]==s[j] :
        i = i + 1
        j = j -1
    return i > j
print (isPalendrom("abcba"))

def f(a:int,b:int)->int : pass
def f(a:float,b:int)->int : pass
def f(a:int,b:float)->int : pass
def f(a:float,b:float)->int : pass
def f(a:int,b:int,c:int)->int : pass
