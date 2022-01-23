import ast
import unittest
import unittest.mock

import asttest
from lib import midterm

class TestDefiningFunctionsCall(asttest.ASTTest):

    def setUp(self):
        super().setUp("question2.py")
        from login import NAME, DNUMBER
        self.k = midterm.k(midterm.xyz(NAME, DNUMBER))
        self.p = midterm.qwerty(midterm.xyz(NAME, DNUMBER))
        lines = self.file.split('\n')
        self.preamble = '\n'.join(lines[:4])
        text = '\n'.join(lines[4:])
        self.tree = ast.parse(text)

    def test_required_syntax(self):
        self.assertEqual(self.preamble, "from lib.midterm import *\nfrom login"
            " import *\ngenerate(NAME, DNUMBER)\n# DO NOT CHANGE ANYTHING "
            "ABOVE THIS LINE", "Do not change anything in the first four lines"
            " given to you in the program.")

    @unittest.mock.patch('sys.stdout')
    def test_results(self, mock_stdout):
        import question2
        self.assertIn(self.p[1], dir(question2), "You did not define the "
                "function correctly. Check its name and parameters and try "
                "again.")
        f = getattr(question2, self.p[1])
        tests = [(1, 10, {0: True, 1: False}), (4, 10, {0: False, 1: False}),
                (5, 15, {0: False, 1: False}), (0, 0, {0: False, 1: False})]
        for test in tests:
            with self.subTest(arguments=test[0:2]):
                result = f(test[0], test[1])
                self.assertEqual(result, test[2][self.k], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0:2], result, test[2][self.k]))


if __name__ == "__main__":
    unittest.main()
