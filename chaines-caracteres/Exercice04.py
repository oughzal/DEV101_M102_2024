def strip(ch:str)->str:
    # return ch.lstrip()
    i = 0
    while ch[i] == " " and i < len(ch):
        i += 1
    j = len(ch) -1
    while ch[j] == " " and j>0:
        j -=1
    return ch[i:j+1]

print(strip("                       DEV     "),"$$$")