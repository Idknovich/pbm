listt={
    "bytes":{
	"0x1":"reg1=arg",
	"0x2":"reg2=arg",
	"0x3":"reg3=arg",
        "0x4":"print(str(reg1))",
        "0x5":"print(str(reg1)+str(reg2))"
    }
}

def getb():
    return listt["bytes"]
