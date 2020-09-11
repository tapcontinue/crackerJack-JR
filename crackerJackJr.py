import re
import fileinput

file_in = open("Copyrights.txt", "rt", newline="\n")
file_out = open("copyright.txt", "wt")

replacements = {
    "Reserved�� ":"Reserved &#160;&#160;&#160;" ,
    " ": " ",#Kills pesty U+000C
    "N� ": "N' ",
    "n� ": "n' ",
    "O� ": "O' ",
    "o� ": "o' ",
    "S� ": "S' ",
    "s� ": "s' ",
    "� ":"&#169; " ,
    "�n ":"'n " ,
    "�n ":"'n " ,
    "^\n{2, 10}":"\n" ,
    "Ⓡ":"&#174;"  ,
    "®":"&#174;"  ,
    "©":"&#169;"  ,
    " & ":" &amp; " ,
    "’":"'",
    "‘": "'",
    "”": "\"",
    "“": "\"",
    "(c)": "&#169;",
    "�m":"'m" ,
    "�t":"'t" ,
    "�v":"'v" ,
    "�� ":" &#160;&#160; " ,
    "�re":"'re" ,
    "�ll":"'ll" ,
    "�&#169; ": " &#160;&#160; ",
    "O�": "O'",
    "�LL": "'LL",
    "�ll": "'ll",
    "�T": "'T",
    "�t": "'t",
    "�M": "'M",
    "�m": "'m",
    "�S": "'S",
    "�s": "'s",
    "   ": "&#160;&#160;&#160;",
    ".  ": ".&#160;",
    "R&H": "R&amp;H",
    "Reserved   Used": "Reserved&#160;&#160;&#160;Used",
    "Secured   All": "Secured&#160;&#160;&#160;All",
    ".  Used": ".&#160;&#160;&#160;Used",
    " b ": " &#9837; ",
    " # ": " &#9839; ",
    }

lines = []
with open('Copyrights.txt') as infile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        lines.append(line)
with open('copyright.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line)
