def alpha(ch : str) -> str:
    s = ""
    for c in ch:
        if (c.lower()>='a' and c.lower()<='z'):
            s += c
    return s
print(alpha("DEV@123@Algo"))