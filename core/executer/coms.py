listt={
    "bytes":{
	"0x1":"reg1=arg",
	"0x2":"reg2=arg",
	"0x3":"reg3=arg",
        "0x4":"print(reg1)",
        "0x5":"print(str(reg1)+str(reg2))",
        "0x6":'exec(f"reg{arg[0]}=reg{arg[1]}")',
        "0x7":"reg1=int(reg1)+int(reg2)",
        "0x8":"if arg str(reg2)==str(reg3):"
    }
}

def getb():
    return listt["bytes"]
