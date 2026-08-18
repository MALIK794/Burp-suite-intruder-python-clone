#!/usr/bin/env python3
def template(ch):
    prefix, _marker, suffix = ch.split("$",2)
    return prefix, _marker, suffix

def sniper(ch):
    if ch!="":
        prefix, _marker, suffix = ch.split("$",2)
        return(f"{_marker}\n")
def Str2Lst(ch):
    l=[]
    suffix=""
    while ch.count("$")!=0:
        preffix, _marker, suffix = template(ch)
        l.extend([preffix,_marker])
        ch=suffix
    l.append(suffix)
    return l
def CompPayload(l,n,word):
    ch=""
    for i in range (len(l)):
        if i!=n :
            ch+=l[i]
        else:
            ch+=f"{word}"
    return ch
print (Str2Lst("this is very $cool$ and $skibbidy$"))
