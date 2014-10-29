
__author__ = 'aortegag'

# Append parent directory when running from command line
import sys
sys.path.append("..")

from re_notation import infix_to_postfix
import unittest

class TestReNotation(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual("+34", infix_to_postfix("3+4"))
        self.assertEqual("++345", infix_to_postfix("(3+4)+5"))
        self.assertEqual("++ab+cd", infix_to_postfix("(a+b)+(c+d)"))
        self.assertEqual("*a", infix_to_postfix("a*"))
        self.assertEqual("*a*b", infix_to_postfix("a*b*"))
        self.assertEqual("+*ab", infix_to_postfix("a*+b"))
        self.assertEqual("+*a*b", infix_to_postfix("a*+b*"))


if __name__ == '__main__':
    unittest.main()