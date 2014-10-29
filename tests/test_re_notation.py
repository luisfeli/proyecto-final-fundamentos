
__author__ = 'aortegag'

# Append parent directory when running from command line
import sys
sys.path.append("..")

from re_notation import infix_to_postfix
import unittest

class TestReNotation(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual("+34", infix_to_postfix("3+4"))
        self.assertEqual("+a+bc", infix_to_postfix("a+b+c"))
        self.assertEqual("+a+b+cd", infix_to_postfix("a+b+c+d"))
        self.assertEqual("++345", infix_to_postfix("(3+4)+5"))
        self.assertEqual("++34+5b", infix_to_postfix("(3+4)+(5+b)"))
        self.assertEqual("+a++34+5b", infix_to_postfix("a+(3+4)+(5+b)"))
        self.assertEqual("+a++34++5bc", infix_to_postfix("a+(3+4)+(5+b)+c"))
        self.assertEqual("+a+x++34+5b", infix_to_postfix("a+x+(3+4)+(5+b)"))
        self.assertEqual("+a+x++34++5b+cy", infix_to_postfix("a+x+(3+4)+(5+b)+c+y"))
        self.assertEqual("++34++5bc", infix_to_postfix("(3+4)+(5+b)+c"))
        self.assertEqual("++34++5b+cy", infix_to_postfix("(3+4)+(5+b)+c+y"))
        self.assertEqual("+++34++5bcy", infix_to_postfix("((3+4)+(5+b)+c)+y"))
        self.assertEqual("+a+x+++34++5bcy", infix_to_postfix("a+x+((3+4)+(5+b)+c)+y"))
        self.assertEqual("++a+x+++34++5bcyu", infix_to_postfix("(a+x+((3+4)+(5+b)+c)+y)+u"))
        self.assertEqual("++ab+cd", infix_to_postfix("(a+b)+(c+d)"))
        self.assertEqual("*a", infix_to_postfix("a*"))
        self.assertEqual("*a", infix_to_postfix("(a*)"))
        self.assertEqual("**a", infix_to_postfix("(a*)*"))
        self.assertEqual("*a.*b", infix_to_postfix("a*b*"))
        self.assertEqual("+*ab", infix_to_postfix("a*+b"))
        self.assertEqual("+*a*b", infix_to_postfix("a*+b*"))
        self.assertEqual("a.b", infix_to_postfix("a b"))
        self.assertEqual("a.b.c.d.e.f", infix_to_postfix("a b     c     d     e    f"))
        self.assertEqual("+a.bc.d", infix_to_postfix("ab + cd"))
        self.assertEqual("+a.b.e+c.df.g", infix_to_postfix("abe + cd + fg"))
        self.assertEqual("+a.b.e+c.df.g.h.i", infix_to_postfix("abe + cd + (fg)(hi)"))
        self.assertEqual("+a.b.e+c.df.g.+h.ij.j", infix_to_postfix("abe + cd + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+c.df.g.+h.ij.j", infix_to_postfix("(abe)* + cd + (fg)(hi + jj)"))
        self.assertEqual("+a*c", infix_to_postfix("a + c* "))
        self.assertEqual("+*ac", infix_to_postfix("a* + c "))
        self.assertEqual("+*a*c", infix_to_postfix("a* + c* "))
        self.assertEqual("+a+*cf", infix_to_postfix("a + c* + f"))
        self.assertEqual("+*a.b.e+*c.df.g.+h.ij.j", infix_to_postfix("(abe)* + c*d + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+c.*df.g.+h.ij.j", infix_to_postfix("(abe)* + cd* + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+*c.df.g.+h.ij.j", infix_to_postfix("(abe)* + (c)*d + (fg)(hi + jj)"))
        self.assertEqual("c.*d", infix_to_postfix("c(d)*"))
        self.assertEqual("*d.c", infix_to_postfix("(d)*c"))
        self.assertEqual("b.*d.c", infix_to_postfix("b.(d)*c"))
        self.assertEqual("+*a.b.e+c.*df.g.+h.ij.j", infix_to_postfix("(abe)* + c(d)* + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+*c.*df.g.+h.ij.j", infix_to_postfix("(abe)* + c*d* + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+*c.*df.g.+h.ij.j", infix_to_postfix("(abe)* + (c)*(d)* + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+*c.x.*d.yf.g.+h.ij.j", infix_to_postfix("(abe)* + (cx)*(dy)* + (fg)(hi + jj)"))
        self.assertEqual("+*a.b.e+*c.x.*d.yf.g.+h.ij.j.*+y.yx.x", infix_to_postfix("(abe)* + (cx)*(dy)* + (fg)(hi + jj)(yy + xx)*"))


if __name__ == "__main__":
        unittest.main()