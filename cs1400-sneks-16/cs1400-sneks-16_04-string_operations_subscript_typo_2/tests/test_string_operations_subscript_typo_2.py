import ast
import unittest

import asttest

class TestStringOperationsSubscriptTypo_2(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_subscript_typo_2.py", False)

    def test_required_syntax(self):
        self.assertNotIn(']"', self.file, "You have a syntax error. Where "
                "should the slice boundaries be positioned?")
        self.tree = ast.parse(self.file)
        subs = self.find_all(ast.Subscript)
        self.assertEqual(len(subs), 1, "You need one subscript.")
        self.assertIsInstance(subs[0].value, ast.Str, "You should be "
                "subscripting a literal value!")
        self.assertEqual(subs[0].value.s, "www.facebook.com", "You should be "
                "subscripting a literal value!")
        self.assertIsInstance(subs[0].slice, ast.Slice, "You need to be using "
                "a subscript (with the colon), not a single index.")
        l = subs[0].slice.lower
        u = subs[0].slice.upper
        self.assertTrue(l != None and u != None, "Your indexes should be "
                "integers.")
        if isinstance(l, ast.Num):
            self.assertEqual(l.n, 4, "Your starting index is not correct.")
        elif isinstance(l, ast.UnaryOp):
            self.assertEqual(l.operand.n, 12, "Your starting index is not "
                    "correct.")
        else:
            self.fail("Your starting index is not correct. Make sure you use a"
                    " literal integer!")
        if isinstance(u, ast.Num):
            self.assertEqual(u.n, 12, "Your ending index is not correct.")
        elif isinstance(u, ast.UnaryOp):
            self.assertEqual(u.operand.n, 4, "Your ending index is not "
                    "correct.")
        else:
            self.fail("Your ending index is not correct. Make sure you use a "
                    "literal integer!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "line.")
        self.assertEqual(self.printed_lines[0], "facebook", "You have printed "
                "the wrong thing.")

if __name__ == "__main__":
    unittest.main()
