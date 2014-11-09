import re_notation
import regex_to_nfa

def main():
    print("Hello world")
    regex1 = re_notation.infix_to_prefix("a+b")
    regex2 = re_notation.infix_to_prefix("a+b*")

    dfa2 = regex_to_nfa.build_dfa(regex2)
    dfa1 = regex_to_nfa.build_dfa(regex1)

    print regex_to_nfa.compare_dfas(dfa1, dfa2)

if __name__ == "__main__":
    main()

