import ast
import unittest

import asttest

class TestConditionalsYesOrNo(asttest.ASTTest):

    def setUp(self):
        super().setUp("conditionals_yes_or_no.py")

    def test_required_syntax(self):
        names = self.find_all(ast.Name)
        for name in names:
            self.assertNotIn(name.id, ["true", "false"], "Remember, you must "
                    "capitialize the first letter in True and False.")
        self.assertEqual(len(names), 1, "You should only use a single "
                "identifier (print) in your solution.")

        bools = self.find_all(ast.NameConstant)
        self.assertEqual(len(bools), 2, "You must use True and False exactly "
                "once each.")
        self.assertEqual(len(self.find_all(ast.Str)), 0, "You should not "
                "have any strings in your program.")
        self.assertEqual(len(self.find_all(ast.Num)), 0, "You should not "
                "have any numbers in your program.")

        boolops = self.find_all(ast.BoolOp)
        self.assertNotEqual(len(boolops), 0, "You will need to use a boolean "
                "operator (or).")
        self.assertEqual(len(boolops), 1, "You should only use a single "
                "boolean operator in your expression.")
        self.assertIsInstance(boolops[0].op, ast.Or, "You must use the "
                "or operator, not the and operator.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        self.assertTrue(self.printed_lines[0], "That is not the correct "
                "result of the boolean expression!")


if __name__ == "__main__":
    unittest.main()
