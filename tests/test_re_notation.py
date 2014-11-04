
__author__ = 'aortegag'

# Append parent directory when running from command line
import sys
sys.path.append("..")

from re_notation import infix_to_prefix
from re_notation import ReNotationException
import unittest

class TestReNotation(unittest.TestCase):
    def test_infix_to_postfix_valid_cases(self):
        self.assertEqual("+34", infix_to_prefix("3+4"))
        self.assertEqual("+a+bc", infix_to_prefix("a+b+c"))
        self.assertEqual("+a+b+cd", infix_to_prefix("a+b+c+d"))
        self.assertEqual("++345", infix_to_prefix("(3+4)+5"))
        self.assertEqual("++34+5b", infix_to_prefix("(3+4)+(5+b)"))
        self.assertEqual("+a++34+5b", infix_to_prefix("a+(3+4)+(5+b)"))
        self.assertEqual("+a++34++5bc", infix_to_prefix("a+(3+4)+(5+b)+c"))
        self.assertEqual("+a+x++34+5b", infix_to_prefix("a+x+(3+4)+(5+b)"))
        self.assertEqual("+a+x++34++5b+cy", infix_to_prefix("a+x+(3+4)+(5+b)+c+y"))
        self.assertEqual("++34++5bc", infix_to_prefix("(3+4)+(5+b)+c"))
        self.assertEqual("++34++5b+cy", infix_to_prefix("(3+4)+(5+b)+c+y"))
        self.assertEqual("+++34++5bcy", infix_to_prefix("((3+4)+(5+b)+c)+y"))
        self.assertEqual("+a+x+++34++5bcy", infix_to_prefix("a+x+((3+4)+(5+b)+c)+y"))
        self.assertEqual("++a+x+++34++5bcyu", infix_to_prefix("(a+x+((3+4)+(5+b)+c)+y)+u"))
        self.assertEqual("++ab+cd", infix_to_prefix("(a+b)+(c+d)"))
        self.assertEqual("*a", infix_to_prefix("a*"))
        self.assertEqual("*a", infix_to_prefix("(a*)"))
        self.assertEqual("**a", infix_to_prefix("(a*)*"))
        self.assertEqual(".*a*b", infix_to_prefix("a*b*"))
        self.assertEqual("+*ab", infix_to_prefix("a*+b"))
        self.assertEqual("+*a*b", infix_to_prefix("a*+b*"))
        self.assertEqual(".ab", infix_to_prefix("a b"))
        self.assertEqual(".a.b.c.d.ef", infix_to_prefix("a b     c     d     e    f"))
        self.assertEqual("+.ab.cd", infix_to_prefix("ab + cd"))
        self.assertEqual("+.a.be+.cd.fg", infix_to_prefix("abe + cd + fg"))
        self.assertEqual("+.a.be+.cd..fg.hi", infix_to_prefix("abe + cd + (fg)(hi)"))
        self.assertEqual("+.a.be+.cd..fg+.hi.jj", infix_to_prefix("abe + cd + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.cd..fg+.hi.jj", infix_to_prefix("(abe)* + cd + (fg)(hi + jj)"))
        self.assertEqual("+a*c", infix_to_prefix("a + c* "))
        self.assertEqual("+*ac", infix_to_prefix("a* + c "))
        self.assertEqual("+*a*c", infix_to_prefix("a* + c* "))
        self.assertEqual("+a+*cf", infix_to_prefix("a + c* + f"))
        self.assertEqual("+*.a.be+.*cd..fg+.hi.jj", infix_to_prefix("(abe)* + c*d + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.c*d..fg+.hi.jj", infix_to_prefix("(abe)* + cd* + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.*cd..fg+.hi.jj", infix_to_prefix("(abe)* + (c)*d + (fg)(hi + jj)"))
        self.assertEqual(".c*d", infix_to_prefix("c(d)*"))
        self.assertEqual(".*dc", infix_to_prefix("(d)*c"))
        self.assertEqual(".b.*dc", infix_to_prefix("b.(d)*c"))
        self.assertEqual("+*.a.be+.c*d..fg+.hi.jj", infix_to_prefix("(abe)* + c(d)* + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.*c*d..fg+.hi.jj", infix_to_prefix("(abe)* + c*d* + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.*c*d..fg+.hi.jj", infix_to_prefix("(abe)* + (c)*(d)* + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.*.cx*.dy..fg+.hi.jj", infix_to_prefix("(abe)* + (cx)*(dy)* + (fg)(hi + jj)"))
        self.assertEqual("+*.a.be+.*.cx*.dy..fg.+.hi.jj*+.yy.xx", infix_to_prefix("(abe)* + (cx)*(dy)* + (fg)(hi + jj)(yy + xx)*"))

    def test_infix_to_postfix_invalid_cases(self):
        self.assertRaises(ReNotationException, infix_to_prefix, "(a")
        self.assertRaises(ReNotationException, infix_to_prefix, "a)")
        self.assertRaises(ReNotationException, infix_to_prefix, "((a)")
        self.assertRaises(ReNotationException, infix_to_prefix, "((a)))")
        self.assertRaises(ReNotationException, infix_to_prefix, "((a)")
        self.assertRaises(ReNotationException, infix_to_prefix, "(abe)* + (c)*d + (fg)hi + jj)")


if __name__ == "__main__":
        unittest.main()