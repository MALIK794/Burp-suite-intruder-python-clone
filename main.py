#!/usr/bin/env python3
from request_template import template
from request_sender import send_one
m=input("what mode would you like to use?\n 1: Sniper\n 2: Pitchfork\n 3: ClusterBomb\nenter the number of mode")
n=int(input("how many payloads?"))
ch=input("Input the template")
if m =="1":
    try:
        with open("wordlist/wordlist1.txt") as f1:
            for a in f1:
                payload=template(ch,a.strip())
                if payload.count("$")%2==0:
                    r=send_one(payload,"http://127.0.0.1:8899/login")
                    print(f" Respone{r}")
                else:
                    print("string delimiter is invalid")
    except FileNotFoundError as e:
        print(f"WARNING:\nwordlist1 not found\nerror:{e}")
