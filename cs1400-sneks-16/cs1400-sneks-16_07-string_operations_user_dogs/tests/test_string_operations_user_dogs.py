import ast
import unittest
from unittest.mock import patch

import asttest

class TestStringOperationsUserDogs(asttest.ASTTest):

    def setUp(self):
        super().setUp("string_operations_user_dogs.py")

    @patch('builtins.input', side_effect=["dogfish"])
    def test_correct_result(self, mock_inputs):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You are not "
                "printing!")
        self.assertIsInstance(self.printed_lines[0], bool, "You are not "
                "printing the right thing. Make sure you print a boolean and "
                "not what the user typed (in this test, the user typed "
                "'dogfish'.")
        self.assertTrue(self.printed_lines[0], "You are printing False when "
                "the user typed 'dogfish'. You should print True in that "
                "case.")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.If)), 0, "You should not use an"
                " if statement for this problem. Instead, keep in mind that "
                "you don't need to print True or False directly. What does a "
                "boolean expression evaluate to?")

        strs = self.find_all(ast.Str)
        self.assertEqual(len(strs), 2, "You need exactly two string literals: "
                "one for the input prompt, and the other to check if 'dog' is "
                "found in what the user typed.")
        self.assertIn("dog", [s.s for s in strs], "You should have the string "
                "literal 'dog' in your program.")

        comps = self.find_all(ast.Compare)
        self.assertEqual(len(comps), 1, "You need to test if the string the "
                "user typed contains another string. What operator can help "
                "you do that? You should only use that one operator.")
        self.assertEqual(len(comps[0].ops), 1, "You should only use a single "
                "operator.")
        self.assertNotIsInstance(comps[0].ops[0], ast.Eq, "You should be using"
                " a different comparison operator. You cannot use the Equals "
                "operator (==) to solve this problem!")
        self.assertIsInstance(comps[0].ops[0], ast.In, "You should be using a "
                "different comparison operator.")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 2, "You should call exactly two "
                "functions: print and input.")
        self.assertEqual(calls[0].func.id, "print", "Call the input function "
                "directly in the print call.")
        self.assertEqual(calls[1].func.id, "input", "Call the input function "
                "directly in the print call.")
        self.assertIn(comps[0], calls[0].args, "Check your placement of the in"
                " operator. It should be used as an argument to print, not "
                "input.")

        self.assertTrue(isinstance(comps[0].left, ast.Str) and
                isinstance(comps[0].comparators[0], ast.Call), "You need to "
                "swap the order of the operands (values) for the in "
                "operator.")
        self.assertIsInstance(comps[0].left, ast.Str, "The left side of the in"
                " operator should be the string 'dog'.")
        self.assertIsInstance(comps[0].comparators[0], ast.Call, "The right "
                "side of the in operator should be the call to input.")
        self.assertEqual(comps[0].comparators[0].func.id, "input", "The right "
                "side of the in operator should be the call to input.")

if __name__ == "__main__":
    unittest.main()
