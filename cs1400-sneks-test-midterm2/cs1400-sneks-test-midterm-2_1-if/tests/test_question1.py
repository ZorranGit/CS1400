import unittest
import unittest.mock
import asttest

class TestQuestion1(asttest.ASTTest):

    def setUp(self):
        super().setUp("question1.py")

    def test_student_status(self):
        func = self.match_signature("student_status", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [(-10, "Freshman"),
                (0, "Freshman"),
                (29, "Freshman"),
                (30, "Sophomore"),
                (31, "Sophomore"),
                (59, "Sophomore"),
                (60, "Junior"),
                (61, "Junior"),
                (89, "Junior"),
                (90, "Senior"),
                (190, "Senior")]
        for test in tests:
            with unittest.mock.patch('sys.stdout'):
                with self.subTest(credits=test[0]):
                    from question1 import student_status
                    result = student_status(test[0])
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given {} it "
                            "returned {}, however, it should have returned {}."
                            .format(repr(test[0]), repr(result), repr(test[1])))

if __name__ == "__main__":
    unittest.main()
