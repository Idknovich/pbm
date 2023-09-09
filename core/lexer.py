def lex(by: bytes):
    
    by=by.split(b"\x00")
    fil=[]
    for byte in by:
        fil.append({"com":hex(byte[0]), "params":byte[1:]})
    return fil

if __name__ == "__main__":
    print(lex(b"\x55\x13\x00\x55"))
