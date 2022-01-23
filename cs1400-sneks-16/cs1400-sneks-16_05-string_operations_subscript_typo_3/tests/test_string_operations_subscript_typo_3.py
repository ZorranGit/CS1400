import ast
import unittest

import asttest

class TestStringOperationsSubscriptTypo_3(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_subscript_typo_3.py")

    def test_required_syntax(self):
        subs = self.find_all(ast.Subscript)
        self.assertEqual(len(subs), 1, "You need one subscript.")
        self.assertEqual(len(self.find_all(ast.List)), 0, "You have created a "
                "new list and subscripted it, instead of subscripting just the"
                " string variable. Pay attention to your square brackets!")
        self.assertIsInstance(subs[0].value, ast.Name, "You should subscript "
                "the letters variable")
        self.assertEqual(subs[0].value.id, "letters", "You should subscript "
                "the letters variable")
        self.assertIsInstance(subs[0].slice, ast.Index, "You should use a "
                "single index, not a slice or anything else.")
        value = subs[0].slice.value
        self.assertIsInstance(value, ast.Num, "Your index should be an integer"
                "literal.")
        self.assertEqual(value.n, 0, "You have the wrong index. What position "
                "refers to the first character in the string?")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                "one line.")
        self.assertNotEqual(self.printed_lines[0], "['ABCDEF']", "You are "
                "creating a new list, instead of subscripting. Check your "
                "syntax!")
        self.assertNotEqual(self.printed_lines[0], "ABCDEF", "You are printing"
                " out the entire string. Just print out the first character.")
        self.assertEqual(self.printed_lines[0], "A", "You printed the wrong "
                "thing. What position refers to the first character in the "
                "string?")

if __name__ == "__main__":
    unittest.main()
