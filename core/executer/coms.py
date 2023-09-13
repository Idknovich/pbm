listt={
    "bytes":{
	"0x1":"reg1='arg'",
	"0x2":"reg2='arg'",
        
	"0x3":"reg3='arg'",
        "0x4":"print(reg1)",
        
        "0x5":"print(str(reg1)+str(reg2))",
        "0x6":'exec(f"reg{str(arg)[0]}=reg{str(arg)[1]}")',
        
        "0x7":"reg1=eval('int(reg1)argint(reg2)')",
        "0x8":"if arg str(reg2)==str(reg3):",
        
        "0x9":"PBM_arg=\"\"",
        "0xa":"PBM_arg=reg3",

        "0xb":"reg3=PBM_arg",
        "0xc":"reg3=input()",

        "0xd":"exit()",
        "0xe":"reg3=[]",

        "0xf":"PBM_arg.append(reg3)"
    }
}

def getb():
    return listt["bytes"]
