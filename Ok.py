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
keys={"62":"Y","64":"U","65":"I",
      "67":"O","69":"P","71":"A","72":"S",
      "74":"D","76":"F","77":"G","79":"H","81":"J",
      "83":"K","84":"L","86":"Z","88":"X","89":"C",
      "91":"V","93":"B","95":"N","96":"M",
      "60":"T","59":"R","57":"E","55":"W","53":"Q",
      "52":"D0","50":"D9","48":"D8","47":"D7","45":"D6","43":"D5","41":"D4","40":"D3","38":"D2","36":"D1",}
upperkeys={"63":"Y","66":"I","68":"O","73":"S","70":"P","75":"D","78":"G","80":"H","82":"J","85":"L",
           "87":"Z","90":"C","92":"V","94":"B","61":"T","58":"E","56":"W","54":"Q","51":"D9","49":"D8",
           "46":"D6","44":"D5","42":"D4","39":"D2","37":"D1",}
for x in lines:
    a=x.split(" ")[0]
    b=x.split(" ")[1]
    if b in keys:
        if a!="0":
            fin.write("DELAY : "+a+"\n"+"Keyboard : "+keys[b]+" : KeyPress\n")
        else:
            fin.write("Keyboard : "+keys[b]+" : KeyPress\n")
        
    elif b in upperkeys:
        if a!="0":
            fin.write("DELAY : "+a+"\n"+"""Keyboard : ShiftLeft : KeyDown
Keyboard : """+upperkeys[b]+""" : KeyPress
Keyboard : ShiftLeft : KeyUp
""")
        else:
            fin.write("""Keyboard : ShiftLeft : KeyDown
Keyboard : """+upperkeys[b]+""" : KeyPress
Keyboard : ShiftLeft : KeyUp
""")
    else: print()
