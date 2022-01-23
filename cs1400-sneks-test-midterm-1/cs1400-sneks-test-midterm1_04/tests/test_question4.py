import ast
import unittest
import unittest.mock

import asttest
from lib import midterm

class TestDefiningFunctionsCall(asttest.ASTTest):

    def setUp(self):
        super().setUp("question4.py")
        from login import NAME, DNUMBER
        self.k = midterm.k(midterm.xyz(NAME, DNUMBER))
        self.p = midterm.qwerty(midterm.xyz(NAME, DNUMBER))
        lines = self.file.split('\n')
        self.preamble = '\n'.join(lines[:4])
        text = '\n'.join(lines[4:])
        self.tree = ast.parse(text)

    def test_required_syntax(self):
        func = self.match_signature('is_surrounded', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameters and try again.")
        self.assertEqual(self.preamble, "from lib.midterm import *\nfrom login"
            " import *\ngenerate(NAME, DNUMBER)\n# DO NOT CHANGE ANYTHING "
            "ABOVE THIS LINE", "Do not change anything in the first four lines"
            " given to you in the program.")

    @unittest.mock.patch('sys.stdout')
    def test_results(self, mock_stdout):
        import question4
        self.assertIn("is_surrounded", dir(question4), "You did not define the "
                "function correctly. Check its name and parameters and try "
                "again.")
        f = getattr(question4, "is_surrounded")
        start = self.p[3]
        end = self.p[4]
        tests = ["Simple text", "shut but not open"+end, start+"open but not shut"]
        for test in tests:
            for base in [("{}", False), (start+"{}"+end, True)]:
                test = base[0].format(test)
                with self.subTest(sentence=test):
                    result = f(test)
                    self.assertEqual(result, base[1], "Your function is "
                            "not returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned '{}'."
                            .format(test, result, base[1]))

if __name__ == "__main__":
    unittest.main()
