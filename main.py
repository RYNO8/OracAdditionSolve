import GetLyrics
import random

words = GetLyrics.getLyrics()

alreadyUsed = []

def make(a,b):
    return "#define %s %s" % (a,b)

def findWorking(s):
    
    for i in range(100):
        nS = ""
        for j in s:
            if random.random() >= 0.5:
                nS += j.upper()
            else:
                nS += j.lower()
        if not nS in alreadyUsed and nS != "and" and nS != "or":
            alreadyUsed.append(nS)
            return nS
    return False

values = [
            "int",
            "main()",
            "{",
            "int",
            "x",
            ";",
            "int",
            "y",
            ";",
            "int",
            "z",
            ";",
            'freopen("addin.txt","r",stdin)',
            ";",
            'freopen("addout.txt","w",stdout)',
            ";",
            "std::cin",
            ">>",
            "x",
            ">>",
            "y",
            ";",
            "z",
            "=",
            "x",
            "+",
            "y",
            ";",
            "std::cout",
            "<<",
            "z",
            "<<",
            "std::endl",
            ";",
            "return",
            "0",
            ";",
            "}"
        ]
finalString = ["#include <bits/stdc++.h>"]

assert(len(words) >= len(values))

for i in range(len(values)):
    finalString.append(make(findWorking(words[i]), values[i]))

finalString.extend(alreadyUsed)
open("output.cpp","w").write("\n".join(finalString))

