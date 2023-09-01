# db5aa067-244a-427b-bd4f-28c6a16d5be4

import sys

def precedence_check(op):
    if op == '/' or op == '*':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return 0

def infix_to_postfix(exp):
    stack = []
    postfixExp = ""
    operators = ['+','-','*','/']
    
    for s in exp:
        if s.isdigit():
            postfixExp += s
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                postfixExp += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()
        elif s in operators:
            while(stack and precedence_check(s) <= precedence_check(stack[-1]) and stack[-1] != "("):
                postfixExp += stack.pop()
            stack.append(s)
    while stack:
        postfixExp += stack[-1]
        stack.pop()
    
    return postfixExp

def evaluate(exp):
    stack = []
    num1, num2, num3 = 0,0,0
    
    for s in exp:
        if s.isdigit():
            stack.append(int(s))
        else:
            if stack:
                num1 = stack.pop()
            if stack:
                num2 = stack.pop()
            if s == '+':
                num3 = num2 + num1
                stack.append(int(num3))
            if s == '-':
                num3 = num2 - num1
                stack.append(int(num3))
            if s == '*':
                num3 = num2 * num1
                stack.append(int(num3))
            if s == '/':
                num3 = num2 / num1
                stack.append(int(num3))
    
    return stack[-1]

for line in sys.stdin:
    print(evaluate(infix_to_postfix(line)))