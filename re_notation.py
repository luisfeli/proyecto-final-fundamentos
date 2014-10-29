__author__ = 'aortegag'


class Precedence:
    PARENTHESIS = 5 # 5 is the highest precedence
    UNION = 4
    KLEENE = 3
    CONCAT = 2


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

    for c in re_expr:
        if is_operator(c):
            if len(stack) > 0 and (c != ")" and c != "(") and (precedence(stack[-1]) < precedence(c) ):
                result += stack.pop()
            elif c is ")":
                while True and len(stack) > 0:
                    next = stack.pop()
                    if next is "(":
                        break
                    result += next
            else:
                stack.append(c)
        else:
            result += c

    while(len(stack)>0): result += stack.pop()

    return result[::-1]
