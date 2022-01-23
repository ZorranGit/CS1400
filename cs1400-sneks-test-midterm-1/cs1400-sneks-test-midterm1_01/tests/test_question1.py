import ast
import unittest
import unittest.mock

import asttest
import lib.midterm as midterm

class TestDefiningFunctionsCall(asttest.ASTTest):

    def setUp(self):
        super().setUp("question1.py", False)
        from login import NAME, DNUMBER
        self.p = midterm.qwerty(midterm.xyz(NAME, DNUMBER))
        lines = self.file.split('\n')
        self.preamble = '\n'.join(lines[:4])
        text = '\n'.join(lines[4:])
        self.tree = ast.parse(text)

    @unittest.mock.patch('sys.stdout')
    def test_required_syntax(self, output):
        #imports = self.find_all(ast.Import)
        #self.assertGreaterEqual(len(imports), 1, "Do not delete the import "
                #"login statement at the top of the file!")
        #self.assertEqual(imports[0].names[0].name, "login", "Do not change or "
                #"delete the import login statement at the top of the file!")
        self.assertEqual(self.preamble, "from lib.midterm import *\nfrom login"
            " import *\ngenerate(NAME, DNUMBER)\n# DO NOT CHANGE ANYTHING "
            "ABOVE THIS LINE", "Do not change anything in the first four lines"
            " given to you in the program.")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 5, "You are not calling the print "
                "function the correct number of times. Make sure you print "
                "one time for each value given in the instructions.")
        for call in calls:
            self.assertIsInstance(call.func, ast.Name, "You should not call "
                    "any function other than print.")
            self.assertEqual(call.func.id, "print", "You should not call any "
                    "function other than print.")

    @unittest.mock.patch('sys.stdout')
    def test_values(self, output):
        calls = self.find_all(ast.Call)
        self.assertGreaterEqual(len(calls), 1, "You are not calling the print "
                "function enough times. Make sure you print one time for each "
                "value given in the instructions.")
        self.assertIsInstance(calls[0].func, ast.Name, "You should not call "
                "any function other than print.")
        self.assertEqual(calls[0].func.id, "print", "You should not call any "
                "function other than print.")
        self.assertEqual(len(calls[0].args), 1, "Your first print should have "
                "exactly one argument.")
        self.assertIsInstance(calls[0].args[0], ast.Num, "The first item to "
                "print should be an integer.")
        self.assertIsInstance(calls[0].args[0].n, int, "The first item to print "
                "should be an integer.")
        self.assertEqual(calls[0].args[0].n, self.p[0], "You are not printing "
                "the first item correctly.")

        self.assertGreaterEqual(len(calls), 2, "You are not calling the print "
                "function enough times. Make sure you print one time for each "
                "value given in the instructions.")
        self.assertIsInstance(calls[1].func, ast.Name, "You should not call "
                "any function other than print.")
        self.assertEqual(calls[1].func.id, "print", "You should not call any "
                "function other than print.")
        self.assertEqual(len(calls[1].args), 1, "Your second print should have"
                " exactly one argument.")
        self.assertIsInstance(calls[1].args[0], ast.Num, "The second item to "
                "print should be a float.")
        self.assertIsInstance(calls[1].args[0].n, float, "The second item to "
                "print should be a float.")
        self.assertEqual(calls[1].args[0].n, float(self.p[1]), "You are not "
                "printing the second item correctly.")

        self.assertGreaterEqual(len(calls), 3, "You are not calling the print "
                "function enough times. Make sure you print one time for each "
                "value given in the instructions.")
        self.assertIsInstance(calls[2].func, ast.Name, "You should not call "
                "any function other than print.")
        self.assertEqual(calls[2].func.id, "print", "You should not call any "
                "function other than print.")
        self.assertEqual(len(calls[2].args), 1, "Your third print should have "
                "exactly one argument.")
        self.assertIsInstance(calls[2].args[0], ast.NameConstant, "The third "
                "item to print should be a boolean.")
        self.assertIsInstance(calls[2].args[0].value, bool, "The third item to "
                "print should be a boolean.")
        self.assertEqual(calls[2].args[0].value, self.p[2], "You are not "
                "printing the third item correctly.")

        self.assertGreaterEqual(len(calls), 4, "You are not calling the print "
                "function enough times. Make sure you print one time for each "
                "value given in the instructions.")
        self.assertIsInstance(calls[3].func, ast.Name, "You should not call "
                "any function other than print.")
        self.assertEqual(calls[3].func.id, "print", "You should not call any "
                "function other than print.")
        self.assertEqual(len(calls[3].args), 1, "Your fourth print should have "
                "exactly one argument.")
        self.assertIsInstance(calls[3].args[0], ast.Str, "The fourth "
                "item to print should be a string.")
        self.assertIsInstance(calls[3].args[0].s, str, "The fourth item to "
                "print should be a string.")
        self.assertEqual(calls[3].args[0].s, self.p[3], "You are not printing "
                "the fourth item correctly.")

        self.assertGreaterEqual(len(calls), 5, "You are not calling the print "
                "function enough times. Make sure you print one time for each "
                "value given in the instructions.")
        self.assertIsInstance(calls[4].func, ast.Name, "You should not call "
                "any function other than print.")
        self.assertEqual(calls[4].func.id, "print", "You should not call any "
                "function other than print.")
        self.assertEqual(len(calls[4].args), 1, "Your fifth print should have "
                "exactly one argument.")
        self.assertIsInstance(calls[4].args[0], ast.NameConstant, "The fifth "
                "item to print should be None.")
        self.assertIsNone(calls[4].args[0].value, "The fifth item to print "
                "should be None.")

    @unittest.mock.patch('sys.stdout')
    def test_output(self, output):
        self.exec_solution()
        self.assertEqual("{}\n{}\n{}\n{}\n{}".format(self.p[0],
                float(self.p[1]), self.p[2], self.p[3], None),
                '\n'.join([str(line) for line in self.printed_lines]),
                "You are not printing the correct result")

if __name__ == "__main__":
    unittest.main()
