def index(ch:str,e:str)->int :
    # return ch.find(e)
    # return ch.index(e) if e in ch else -1
    for i in range(len(ch)):
        if ch[i] ==e :
            return i
    return -1


print(index("DEV101","H"))