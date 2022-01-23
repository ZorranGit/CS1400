import ast
import unittest

import asttest

class TestConditionalsSimpleComparison(asttest.ASTTest):

    def setUp(self):
        super().setUp("conditionals_simple_comparison.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        legal = [-5, 5]
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertIn(numbers[0].n, legal, "You should use the numbers -5 and "
                "5 exactly once each in your expression.")
        self.assertIn(numbers[1].n, legal, "You should use the numbers -5 and "
                "5 exactly once each in your expression.")

        strings = self.find_all(ast.Str)
        self.assertEqual(len(strings), 0, "You should not have any strings in "
                "your program.")

        compares = self.find_all(ast.Compare)
        self.assertEqual(len(compares), 1, "You need to use exactly one "
                "comparison operator.")
        self.assertEqual(len(compares[0].ops), 1, "You need to use exactly one "
                "comparison operator.") # chained operators
        self.assertIsInstance(compares[0].ops[0], ast.Lt, "You should be "
                "using the less than operator (<).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        self.assertTrue(self.printed_lines[0], "That is not the correct "
                "result of the comparison!")

if __name__ == "__main__":
    unittest.main()
