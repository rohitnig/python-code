string=input()
prevChar = ""
curr_longest = ""
longest = ""

for char in string:
    if (prevChar.upper()<=char.upper()):
        curr_longest += char
        if len(curr_longest) > len(longest):
            longest= curr_longest
    else:
        curr_longest = char
    prevChar = char
print( longest )
