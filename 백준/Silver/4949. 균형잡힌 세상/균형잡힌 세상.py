import sys

input = sys.stdin.readline

while 1:
    str = input()
    stack = []
    if str[0] != '.' :
        i = 0
        err = 0
        while str[i] != '.':
            if str[i] == '(':
                stack.append('(')
            if str[i] == ')' :
                if stack and stack[-1] == '(':
                    stack.pop()
                else :
                    print("no")
                    err = 1
                    break
            if str[i] == '[':
                stack.append('[')
            if str[i] == ']' :
                if stack and stack[-1] == '[':
                    stack.pop()
                else :
                    print("no")
                    err = 1
                    break
            i += 1
        if not err:
            if stack :
                print("no")
            else :
                print("yes")
    else :
        exit()