import ast
import unittest
import unittest.mock
import asttest

class TestQuestion3(asttest.ASTTest):

    def setUp(self):
        super().setUp("question3.py")

    def test_student_status(self):
        func = self.match_signature("count_me", 2)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameters and try again.")

        calls = self.find_method_calls("count") + self.find_function_calls("Counter") + self.find_function_calls("len")
        for call in calls:
            name = ""
            if isinstance(call.func, ast.Name):
                name = call.func.id
            elif isinstance(call.func, ast.Attribute):
                name = call.func.attr
            self.fail("You are not allowed to use the {} function for this "
                    "question.".format(name))

        tests = [((["burrito", "taco", "burrito", "nachos"], "burrito"), 2),
                (([], 0), 0),
                (([1, 2, 3], 4), 0),
                (([True, True, True, False], True), 3),
                (([None, None, None], None), 3),
                ((["a", "b", "c", "d"], "d"), 1)]

        for test in tests:
            with unittest.mock.patch('sys.stdout'):
                with self.subTest(a_list=test[0][0], value=test[0][1]):
                    from question3 import count_me
                    result = count_me(test[0][0], test[0][1])
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given {} it "
                            "returned {}, however, it should have returned {}."
                            .format(repr(test[0]), repr(result), repr(test[1])))

if __name__ == "__main__":
    unittest.main()
