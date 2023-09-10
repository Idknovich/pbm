listt={
    "bytes":{
	b"\x01":"reg1=arg",
	b"\x02":"reg2=arg",
	b"\x03":"reg3=arg",
        b"\x04":"print(reg1)",
        b"\x05":"print(str(reg1)+str(reg2))"
    }
}

def getb():
    return listt["bytes"]
