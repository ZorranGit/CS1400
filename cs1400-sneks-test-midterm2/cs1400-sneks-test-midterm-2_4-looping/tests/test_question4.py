import unittest
import unittest.mock
import asttest

class TestQuestion4(asttest.ASTTest):

    def setUp(self):
        super().setUp("question4.py")

    def test_student_status(self):
        func = self.match_signature("maximum", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        calls = self.find_function_calls("max")
        self.assertEqual(len(calls), 0, "You are not allowed to use the max "
                "function for this question.")

        tests = [([], None),
                ([1,1,1,1], 1),
                ([1,2,3,4,5], 5),
                ([5,4,3,2,1], 5),
                ([10], 10),
                ([1, 100, 1], 100)]
        for test in tests:
            with unittest.mock.patch('sys.stdout'):
                with self.subTest(a_list=test[0]):
                    from question4 import maximum
                    result = maximum(test[0])
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given {} it "
                            "returned {}, however, it should have returned {}."
                            .format(repr(test[0]), repr(result), repr(test[1])))

if __name__ == "__main__":
    unittest.main()
