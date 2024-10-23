S = "DEV101"
print(S[1])
# S[0]= "F" # immutable
S = "DEVOAM201"
S2 = 'DEV'
print(S[0:3])

D = "DEV" + "101"
S = "AB"*6
print(S)
print("DF" not in "DEV101")
print(S[3])
S = "DEV101"
print(S[0:4])
print(S[0:])
print(S[:4])
print(S[:])
print(S[-1:-5:-1])
print(S[::-1])

print("abc".upper())
print("ABC".lower())
print("abc efg".title())
print("aBc EFg".swapcase())
S = "          DEV101         "
print(S.rstrip(),"*") # trim
print("DEV101 DEV101".rfind("101"))
print("DEV101 DEV101".replace("101","201"))
H =2
M = 5
S = 2
print(f"{str(H).zfill(2)}:{str(M).zfill(2)}:{str(S).zfill(2)}")
print("abc".center(20),"***")
print("abc".rjust(20),"***")

S = "ABC,EF,H,KTH,TREZ"
L = S.split(",")
print(L)
S ="23/10/2024"
D = S.split("/")
print(D)
J = int(D[0])
M = int(D[1])
A = int(D[2])

S = """
DEV
101
DEOAM
201
"""
print(S.splitlines())
print("DEV101".lower().startswith("dev"))
print("DEV".lower() == "dEv".lower())