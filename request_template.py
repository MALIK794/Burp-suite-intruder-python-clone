#!/usr/bin/env python3

template = "long $aah$ string"
prefix, _marker, suffix = template.split("$")

with open("wordlist.txt", "r") as f1, open("output.txt", "w") as f2:
    for line in f1:
        word = line.strip()
        if not word:
            continue
        f2.write(f"{prefix}{word}{suffix}\n")
