import ast
import unittest

import asttest

class TestConditionalsLies(asttest.ASTTest):

    def setUp(self):
        super().setUp("conditionals_lies.py")

    def test_required_syntax(self):
        names = self.find_all(ast.Name)
        for name in names:
            self.assertNotEqual(name.id, "false", "Remember, you must "
                    "capitialize the first letter in False. But you "
                    "shouldn't be using False for this problem anyway.")
            self.assertNotEqual(name.id, "true", "Remember, you must "
                    "capitialize the first letter in True.")
        self.assertNotEqual(len(names), 0, "You should print the result of "
                "your boolean expression.")
        self.assertEqual(len(names), 1, "The only identifier you should have"
                "in your solution is print.")

        bools = self.find_all(ast.NameConstant)
        self.assertEqual(len(bools), 1, "You need exactly one boolean for "
                "this problem.")
        self.assertIsNotNone(bools[0].value, "You should not use the value "
                "None for this problem.")
        self.assertTrue(bools[0].value, "You should not use the boolean "
                "literal False in your solution.")
        self.assertEqual(len(self.find_all(ast.Str)), 0, "You should not "
                "have any strings in your program.")
        self.assertEqual(len(self.find_all(ast.Num)), 0, "You should not "
                "have any numbers in your program.")

        unarys = self.find_all(ast.UnaryOp)
        self.assertNotEqual(len(unarys), 0, "You will need to use the not "
                "operator.")
        self.assertEqual(len(unarys), 1, "You should only use one not "
                "operator.")
        self.assertIsInstance(unarys[0].op, ast.Not, "You will need to use "
                "the not operator.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        self.assertFalse(self.printed_lines[0], "That is not the correct "
                "result of the boolean expression!")

if __name__ == "__main__":
    unittest.main()
