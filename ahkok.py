import sys
import time
fil=sys.argv[1]
midiorg=open(fil)
lines=[]
a=midiorg.readline()
print(a)
while a!="":
    if "On ch=1" in a:
        if "v=0" not in a:
            line=a.split(" ")
            tick=line[0]
            smol=line[3].split("=")
            key=smol[1]
            great=(tick+" "+key)
            lines.append(great)
            a=midiorg.readline()
        else : a=midiorg.readline()
    else : a=midiorg.readline()
def b(lines):
    return int(lines.split(" ")[0])

lines=sorted(lines,key=b)
a=0
c=0
for x in lines:
    b=x.split(" ")[0]
    d=x.split(" ")[1]
    b=int(b)
    x=b-a
    x=str(x)
    lines[c]=x+" "+d
    c+=1
    a=b


midiorg.close()
fin=open(fil,"w")
keys={"62":"y","64":"u","65":"i",
      "67":"o","69":"p","71":"a","72":"s",
      "74":"d","76":"f","77":"g","79":"h","81":"j",
      "83":"k","84":"l","86":"z","88":"x","89":"c",
      "91":"v","93":"b","95":"n","96":"m",
      "60":"t","59":"r","57":"e","55":"w","53":"q",
      "52":"0","50":"9","48":"8","47":"7","45":"6","43":"5","41":"4","40":"3","38":"2","36":"1",
      "63":"+y","66":"+i","68":"+o","73":"+s","70":"+p","75":"+d","78":"+g","80":"+h","82":"+j","85":"+l",
        "87":"+z","90":"+c","92":"+v","94":"+b","61":"+t","58":"+e","56":"+w","54":"+q","51":"+9","49":"+8",
        "46":"+6","44":"+5","42":"+4","39":"+2","37":"+1"}
fin.write("""; #NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
; SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
; SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
+`::
""")
#start here

for x in lines:
    a=x.split(" ")[0]
    a=int(a)
    a*=1
    a=str(a)
    b=x.split(" ")[1]
    c=0
    if b in keys:
        if a!="0":
            fin.write("Send "+keys[b]+"""
Sleep """+a+"\n")
        else:
            fin.write("Send "+keys[b]+"\n")
    else: print()

#end here
fin.write("""^b::pause
return""")
