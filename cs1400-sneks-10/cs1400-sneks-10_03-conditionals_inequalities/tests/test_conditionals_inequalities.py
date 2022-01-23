import ast
import unittest

import asttest

class TestConditionalsInequalities(asttest.ASTTest):

    def setUp(self):
        super().setUp("conditionals_inequalities.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        self.assertEqual(len(numbers), 4, "You should only use the numbers 1 "
                "and 2 twice each in your code.")
        for num in numbers:
            if num.n not in [1, 2]:
                self.fail("You should only use the numbers 1 and 2 twice each "
                        "in your code.")

        self.assertEqual(len(self.find_all(ast.Str)), 0, "You should not use "
                "any strings in this problem.")
        self.assertEqual(len(self.find_all(ast.NameConstant)), 0, "You should not use "
                "any boolean values or None values in this problem.")

        boolops = self.find_all(ast.BoolOp)
        self.assertNotEqual(len(boolops), 0, "You will need to use a boolean "
                "operator (and).")
        self.assertEqual(len(boolops), 1, "You should only use a single "
                "boolean operator in your expression.")
        self.assertIsInstance(boolops[0].op, ast.And, "You must use the and "
                "operator, not the or operator.")

        compares = self.find_all(ast.Compare)
        self.assertEqual(len(compares), 2, "You are not making the right "
                "number of comparisons!")
        for comp in compares:
            self.assertEqual(len(comp.ops), 1, "You are not making the right "
                    "number of comparisons!") # chained operators
            self.assertIsInstance(comp.ops[0], ast.NotEq, "You must use the "
                    "not equal (!=) operator.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        self.assertTrue(self.printed_lines[0], "That is not the correct "
                "result of the boolean operation!")

if __name__ == "__main__":
    unittest.main()
