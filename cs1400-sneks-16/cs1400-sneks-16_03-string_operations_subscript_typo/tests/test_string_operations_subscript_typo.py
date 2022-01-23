import ast
import unittest

import asttest

class TestStringOperationsSubscriptTypo(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_subscript_typo.py")

    def test_required_syntax(self):
        subs = self.find_all(ast.Subscript)
        self.assertEqual(len(subs), 1, "You need to keep the subscript there, "
                "just change it to correctly grab the last character of the "
                "string.")
        self.assertIsInstance(subs[0].value, ast.Str, "Please don't change the"
                " original string. It should be \"Python\".")
        self.assertEqual(subs[0].value.s, "Python", "Please don't change the "
                "original string. It should be \"Python\".")
        self.assertIsInstance(subs[0].slice, ast.Index, "You should still use "
                "an index to grab the last character. No need to slice or "
                "anything else.")
        value = subs[0].slice.value
        if isinstance(value, ast.Num):
            self.assertNotEqual(value.n, 6, "You should change the index to "
                    "properly grab the last character.")
            self.assertEqual(value.n, 5, "That is not the correct index. At "
                    "what position is the last character?")
        elif isinstance(value, ast.UnaryOp):
            self.assertIsInstance(value.operand, ast.Num, "The index should be"
                    " an integer literal.")
            self.assertEqual(value.operand.n, 1, "That is not the correct "
                    "index. At what position is the last character?")
        else:
            self.fail("The index should be an integer literal.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        self.assertEqual(self.printed_lines[0], "n", "You printed the wrong "
                "thing.")

if __name__ == "__main__":
    unittest.main()
