import ast
import unittest

import asttest

class TestStringOperationsGrabAnimal(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_grab_animal.py")

    def test_required_syntax(self):
        subs = self.find_all(ast.Subscript)
        self.assertEqual(len(subs), 1, "You need one subscript.")
        self.assertIsInstance(subs[0].value, ast.Name, "You should be "
                "subscripting the animals variable.")
        self.assertEqual(subs[0].value.id, "animals", "You should be "
                "subscripting the animals variable.")
        self.assertIsInstance(subs[0].slice, ast.Slice, "You need to be using "
                "a subscript (with the colon), not a single index.")
        l = subs[0].slice.lower
        u = subs[0].slice.upper
        self.assertIsNotNone(l, "You need to specify a start index.")
        self.assertIsInstance(l, ast.Num, "You should use a literal integer "
                "for the start index.")
        self.assertIn(l.n, (4, -9), "Your starting index is not correct.")
        self.assertIsNotNone(u, "You need to specify an end index.")
        self.assertIsInstance(u, ast.Num, "You should use a literal integer "
                "for the end index.")
        self.assertIn(u.n, (7, -6), "Your ending index is not correct.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        self.assertEqual(self.printed_lines[0], "dog", "You have printed the "
                "wrong thing.")

if __name__ == "__main__":
    unittest.main()
