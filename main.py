#import GetLyrics
import random

words = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
(Ooh) Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry"""
#words = GetLyrics.getLyrics()
words = input("Enter words: ")
words = words.replace(",", "").replace("\n", " ").replace("(", "").replace(")", "").replace("'", "").split(" ")

alreadyUsed = []

def make(a,b):
    return "#define %s %s" % (a,b)

global count
count = 1

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
    globals()["count"] += 1
    return s + "_" * count

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
while len(values) < len(words): values.append(";")

finalString = ["#include <bits/stdc++.h>"]

assert(len(words) >= len(values))

for i in range(len(values)):
    finalString.append(make(findWorking(words[i]), values[i]))

with open("output.cpp","w") as f:
    f.write("\n".join(finalString))
    f.write("\n")
    f.write(" ".join(alreadyUsed))

