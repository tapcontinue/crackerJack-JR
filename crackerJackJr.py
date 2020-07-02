import re

file_in = open("Copyrights.txt", "rt", newline="\n")
file_out = open("copyright.txt", "wt")


oldStrings = (
"Reserved�� ",
"� ",
"\n{2, 10}",
"Ⓡ",
"®",
"©",
" & ",
"�m",
"�t",
"�v",
"�� ",
"�re",
"�ll",
"�&#169; ",
"O�",
"�LL",
"�M",
"�s",
"�S",
)

newStrings = (
"Reserved &#160;&#160;&#160;",
"&#169; ",
"\n",
"&#174;" ,
"&#174;" ,
"&#169;" ,
" &amp; ",
"'m",
"'t",
"'v",
" &#160;&#160; ",
"'re",
"'ll",
" &#160;&#160; ",
"O'",
"'LL",
"'M",
"'s",
"'S",
)

for line in file_in:
    for check, rep in zip(oldStrings, newStrings):
        line = line.replace(check, rep)
    file_out.write(line)

file_in.close()
file_out.close()
