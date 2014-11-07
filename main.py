import re_notation
import regex_to_nfa

def build_dfa(regex):
    """receives a regex in prefix notation and returns
    the equivalent DFA"""
    regex = regex[::-1]
    stack = []

    for symbol in regex:
        if symbol.isalnum():
            symbol_nfa = regex_to_nfa.NFA()
            symbol_nfa.init_from_symbol(symbol)
            stack.append(symbol_nfa)
        elif symbol == '.':
            op1 = stack.pop()
            op2 = stack.pop()
            nfa = regex_to_nfa.nfa_concatenation(op1, op2)
            stack.append(nfa)
        elif symbol == '+':
            op1 = stack.pop()
            op2 = stack.pop()
            nfa = regex_to_nfa.nfa_union(op1, op2)
            stack.append(nfa)
        elif symbol == '*':
            op = stack.pop()
            nfa = regex_to_nfa.nfa_kleene_star(op)
            stack.append(nfa)

        else:
            print "ERROR: Unkown symbol {0}\n".format(symbol)
            return -1

    nfa = stack.pop()
    if stack:
        print "ERROR: stack is not empty\n"
        return -1

    nfa = regex_to_nfa.remove_empty_transitions(nfa)
    dfa = regex_to_nfa.nfa_to_dfa(nfa)
    return dfa


def main():
    print("Hello world")
    regex1 = re_notation.infix_to_prefix("a+b")
    regex2 = re_notation.infix_to_prefix("(a+b)*")

    dfa2 = build_dfa(regex2)
    dfa1 = build_dfa(regex1)

    print regex_to_nfa.compare_dfas(dfa1, dfa2)

if __name__ == "__main__":
    main()

