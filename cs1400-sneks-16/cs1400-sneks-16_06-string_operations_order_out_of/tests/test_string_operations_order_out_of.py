import ast
import unittest

import asttest

class TestStringOperationsOrderOutOf(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_order_out_of.py")

    def test_required_syntax(self):
        strs = self.find_all(ast.Str)
        if len(strs) == 2:
            self.assertNotEqual(strs[1].s, " ", "Remember you cannot use any "
            "string literals in your expression. Instead, try subscripting the"
            " original variable to just grab a single space.")
        self.assertEqual(len(strs), 1, "You can only use one string literal.")
        self.assertEqual(strs[0].s, "order out of", "Do not change the "
                "original string literal value.")

        subs = self.find_all(ast.Subscript)
        self.assertGreaterEqual(len(subs), 2, "You'll want to write more "
                "subscripting expressions than that!")
        self.assertLessEqual(len(subs), 5, "You can use at most five "
                "subscripts (but it's possible with just three).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        self.assertNotEqual(self.printed_lines[0], "out of order ", "There's "
                "an extra space at the end!")
        self.assertNotEqual(self.printed_lines[0], "out oforder", "Don't "
                "forget to put a space between the two substrings!")
        self.assertEqual(self.printed_lines[0], "out of order", "You are not "
                "quite printing the right result. Look closely at the expected"
                " output and what your program is printing.")

if __name__ == "__main__":
    unittest.main()
