import ast
import unittest

import asttest

class TestStringOperationsBossMistake(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_boss_mistake.py")

    def test_required_syntax(self):
        subs = self.find_all(ast.Subscript)
        self.assertEqual(len(subs), 1, "You need one subscript.")
        self.assertIsInstance(subs[0].value, ast.Name, "Write your subcript on"
                "the example_client_name variable.")
        self.assertEqual(subs[0].value.id, "example_client_name", "You should "
                "be subscripting the example_client_name variable.")
        self.assertIsInstance(subs[0].slice, ast.Slice, "You need to be using "
                "a subscript (with the colon), not a single index.")

        l = subs[0].slice.lower
        u = subs[0].slice.upper
        self.assertTrue(l is None or (isinstance(l, ast.Num) and l.n == 0),
                "Your starting index is not correct. How do you specify all "
                "the but the last 10 characters?")
        if isinstance(l, ast.Num):
            self.assertNotEqual(l.n, -10, "Your starting index is not correct."
                    " You are correct that you need -10, but it does not "
                    "belong on the left.")
        self.assertIsNotNone(u, "Your ending index is not correct. You are "
                "correct, however, that one side of the slice should be "
                "blank.")
        self.assertNotIsInstance(u, ast.Num, "Your starting index is not "
                "correct. Although your subscript might work for this specific"
                " value, what would happen on a shorter name? You need to "
                "subscript names of any length!")
        self.assertIsInstance(u, ast.UnaryOp, "The ending index should be an "
                "integer literal.")
        self.assertNotEqual(u.operand.n, 11, "Your ending index is not correct, but "
                "you are very close. You need to remove one fewer characters!")
        self.assertEqual(u.operand.n, 10, "Your ending index is not correct. How do "
                "you specify all the way to the end of the string?")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        self.assertEqual(self.printed_lines[0], "Dan Danielson", "You have "
                "printed the wrong thing.")

if __name__ == "__main__":
    unittest.main()
