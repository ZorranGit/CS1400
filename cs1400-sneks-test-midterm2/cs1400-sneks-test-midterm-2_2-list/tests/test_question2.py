import ast
import unittest
import unittest.mock

import asttest

class TestQuestion2(asttest.ASTTest):

    def setUp(self):
        super().setUp("question2.py")

    def test_student_status(self):
        func = self.match_signature("midpoint", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        ifs = self.find_all(ast.If, func)
        self.assertLess(len(ifs), 2, "You are not allowed to use more than one"
                " if statement for this question. Consider how to calculate "
                "the middle index in a general sense.")

        tests = [([], None),
                ([1], 1),
                (["a", "B"], "B"),
                ([False, False, True], False),
                ([None, True, -1, "z"], -1),
                ([0, 0, 1, 0, 0], 1)]

        for test in tests:
            with unittest.mock.patch('sys.stdout'):
                with self.subTest(a_list=test[0]):
                    from question2 import midpoint
                    result = midpoint(test[0])
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given {} it "
                            "returned {}, however, it should have returned {}."
                            .format(repr(test[0]), repr(result), repr(test[1])))

if __name__ == "__main__":
    unittest.main()
