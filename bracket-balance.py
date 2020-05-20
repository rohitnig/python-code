#take input
inp=input()

brackets = { '[' : ']', '{' : '}', '(' : ')' }

if len(inp) % 2 != 0:
    print ('No')
    exit()
else:
    stack = []
    for ch in inp:
        if ch in list(brackets.keys()):
            stack.append(ch)
        else:
            if len(stack) <= 0:
                print ('No')
                exit()
            elif stack[-1] in list(brackets.keys()) and brackets[stack[-1]] == ch:
                stack.pop()
            else:
                print ('No')
                exit()

if len(stack)==0:
    print ('Yes')
else:
    print ('No')

