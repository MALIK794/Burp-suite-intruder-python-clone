#!/usr/bin/env python3
import sys
from request_template import *
from request_sender import send_one
#note that exit code 0 means the program was executed properly while 1 mean a file was not found and 2 mean a delimiter error
m=input("what mode would you like to use?\n 1: Sniper\n 2: Pitchfork\n 3: ClusterBomb\nenter the number of mode")
ch=input("Input the template \n")
if m =="1":
    n=ch.count("$")//2
    #this block handles the case of ch being empty
    if ch=="":
        try:
            with open(f"wordlist/wordlist1.txt") as f1:
                for a in f1:
                    r=send_one(a.strip(),"http://127.0.0.1:8899/login")
                    print(f" Respone{r}")
            sys.exit(0)
        except FileNotFoundError as e:
            print(f"WARNING: wordlist1 not found\nerror:{e}")
            sys.exit(1)
    elif n==0:
        #this block is pretty self-explanatory 
        print("string contains no delimiter")
        sys.exit(2)
    try:
        #this is the main use case of this program
        if ch.count("$")%2==0:
            with open("wordlist/wordlist1.txt") as f1:
                for a in f1:
                    for i in range (1,n+1):
                        print(i)
                        l=Str2Lst(ch)
                        payload=CompPayload(l,i*2-1,a.strip())
                        print(payload)
                        r=send_one(payload,"http://127.0.0.1:8899/login")
                        print(f" Respone{r}")
            sys.exit(0)
        else:
            print("string delimiter is invalid")
            sys.exit(2)
    except FileNotFoundError as e:
        print(f"WARNING:\nwordlist1 not found\nerror:{e}")
        sys.exit(1)
