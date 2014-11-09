__author__ = 'aortegag'

# Append parent directory when running from command line
import sys
sys.path.append("..")

import unittest
from re_notation import infix_to_prefix
from regex_to_nfa import build_dfa
from regex_to_nfa import compare_dfas

class TestRegexToNfa(unittest.TestCase):
    def test_valid_tests(self):
        f = lambda reg: build_dfa(infix_to_prefix(reg))
        compare = lambda r1, r2: compare_dfas(f(r1), f(r2))
        tup = (True, "dfa1 and dfa2 accept the same language")

        self.assertEqual(tup, compare("a", "a"))
        self.assertEqual(tup, compare("a(a+b)*bb", "a(b+a)*bb"))
        self.assertEqual(tup, compare("(a+b)* b (a+b)* b (a+b)*", "a* b a* b (a+b)*"))
        self.assertEqual(tup, compare("(0+11*0)*", "(0+11*0)*+(11*0)*00*"))
        self.assertEqual(tup, compare("(0+11*0)*", "0*1(1+00*1)*00* + 0*"))

        # The following tests I THINK are equal. Please take a look at them
        # They are failing
        self.assertEqual(tup, compare("a", "#a"))
        self.assertEqual(tup, compare("a", "a#"))
        self.assertEqual(tup, compare("a", "#a#"))
        self.assertEqual(tup, compare("a*", "a*#"))
        self.assertEqual(tup, compare("a*", "#a*"))
        self.assertEqual(tup, compare("a*", "#a*#"))
        self.assertEqual(tup, compare("#", "##"))
        self.assertEqual(tup, compare("a+ab", "a(#+b)"))
        self.assertEqual(tup, compare("(11*0+00*11*0)*(00*)", "((1+00*1)1*0)*(00*)"))
        self.assertEqual(tup, compare("(a+(a+b)b)*", "a*(a+b)ba* + a*"))

    def test_invalid_tests(self):
        f = lambda reg: build_dfa(infix_to_prefix(reg))
        compare = lambda r1, r2: compare_dfas(f(r1), f(r2))
        tup = (True, "dfa1 and dfa2 accept the same language")

        self.assertNotEqual(tup, compare("a", "a"))
        self.assertNotEqual(tup, compare("a(a+b)*bb", "a(b+a)*bbb"))
        self.assertNotEqual(tup, compare("(a+b)* b (a+b)* b (a+b)*", "a* b a* b (a+b)*aa"))
        self.assertNotEqual(tup, compare("(0+11*0)*", "(0+11*0)*+(11*0)00*"))
        self.assertNotEqual(tup, compare("(0+11*0)*", "0*1(1+00*1)*00* + 0"))
