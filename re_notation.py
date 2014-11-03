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


def add_concatenation_dot(s):
    pattern = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9]|\)\(|\*[a-zA-Z0-9]|\*\(|[a-zA-Z0-9]\(')
    res = pattern.search(s)
    while(res):
        target_str = res.group()
        s = re.sub(pattern, target_str[0]+"."+target_str[1], s, count=1)
        res = pattern.search(s)
    return s

def infix_to_prefix(re_expr):
    stack = []
    result = ""
    re_expr = re.sub(r'\s+', '', re_expr)
    re_expr = add_concatenation_dot(re_expr)
    original = re_expr
    re_expr = invert_parenthesis(re_expr[::-1]) # reverse string and the invert parenthesis


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

            while len(stack) > 0 and (precedence(stack[-1]) >= precedence(c)) and stack[-1] != "(":
                top = stack.pop()
                if top != "(" and top != ")":
                    if result[-1] == ".":
                        result = result[0:-1] + top + "."
                    else:
                        result += top
            stack.append(c)
        else:
            if len(stack)>0 and c == "." and stack[-1] == "*": #when concatenating a kleene
                result += stack.pop() + c
            else:
                result += c

    while(len(stack)>0): result += stack.pop()

    return result[::-1]
