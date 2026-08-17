#!/usr/bin/env python3
def template(ch,word):
    if ch!="":
        prefix, _marker, suffix = ch.split("$",2)
        return(f"{prefix}{word}{suffix}\n")
    else:
        return word.strip()
