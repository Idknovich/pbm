listt={
    "bytes":{
	"0x1":"reg1=aarg",
	"0x2":"reg2=aarg",
        
	"0x3":"reg3=aarg",
        "0x4":"print(reg1)",
        
        "0x5":"print(str(reg1)+str(reg2))",
        "0x6":'exec(f"reg{arg[0]}=reg{arg[1]}")',
        
        "0x7":"reg1=int(reg1)+int(reg2)",
        "0x8":"if arg str(reg2)==str(reg3):",
        
        "0x9":"exec('PBM_arg=\"\"')",
        "0xa":"exec(f'PBM_{reg1}=aarg')",

        "0xb":"exec(f'reg3=PBM_{arg}')"
    }
}

def getb():
    return listt["bytes"]
