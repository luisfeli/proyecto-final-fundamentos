__author__ = 'aortegag'
import re

class Precedence:
    PARENTHESIS = 5 # 5 is the highest precedence
    KLEENE = 4
    CONCAT = 3
    UNION = 2


def precedence(op):
    if op == "(" or op == ")":
        return Precedence.PARENTHESIS
    if op == "+":
        return Precedence.UNION
    if op == "*":
        return Precedence.KLEENE
    return Precedence.CONCAT


def is_operator(c):
    if c == '(' or c == ')' or c == '*' or c == "+":
        return True
    return False


def invert_parenthesis(s):
    result = ""
    for c in s:
        if c == "(": result += ")"
        elif c == ")": result += "("
        else: result += c

    return result


def infix_to_postfix(re_expr):
    stack = []
    result = ""
    re_expr = invert_parenthesis(re_expr[::-1]) # reverse string and the invert parenthesis
    re_expr = re.sub(r'\s+', '', re_expr)

    for c in re_expr:
        if is_operator(c):
            if c is "(":
                stack.append(c)
                continue

            if c is ")":
                while True and len(stack) > 0:
                    next = stack.pop()
                    if next is "(":
                        break
                    result += next
                continue

            if len(stack) > 0 and (precedence(stack[-1]) >= precedence(c)) and stack[-1] != "(":
                top = stack.pop()
                if top != "(" and top != ")":
                    result += top
                stack.append(c)
                continue

            else:
                stack.append(c)
        else:
            result += c

    while(len(stack)>0): result += stack.pop()

    return result[::-1]
