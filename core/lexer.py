def lex(by: bytes):
    
    by=by.split(b"\x00")
    fil=[]
    for byte in by:
        fil.append({"com":byte[0], "params":byte[1:len(by-1)]
    return fil

print(lex(b"\x25\x55\x00\x24"))
