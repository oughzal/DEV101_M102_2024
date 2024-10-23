def deleteSpace(ch:str)->str:
    # return " ".join(ch.split())
    i =0
    s = ""
    while i <len(ch):
        if ch[i] != " ":
            s += ch[i]
            i += 1
        else:
            s += " "
            while ch[i] == " ":
                i += 1
        
    return s


print(deleteSpace("DEV    101  Algo     python"))