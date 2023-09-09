def lex(by: bytes):
    by=by.split(b"\x00")
    print(by)

lex(b"\x25\x55\x00\x24")
