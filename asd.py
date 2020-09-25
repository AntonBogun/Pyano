import sys
import time
x=input()
while x:
    if x=="a":
        print("hello world")
        x=input()
    elif x=="b":
        print("ok")
        x=input()
    elif x!="":
        x=input()
print(x)
y=0
if y==0:
    y+=1
    if y==1:
        print("B")

def helloworld():
    print("hello world")
    
def ok():
    print("ok")
map = {"a":helloworld,"b":ok}
def check(x):
    map[x]()
x=input()
while x:
    if x!="":
        check(x)
        x=input()
