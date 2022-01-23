import unittest
import asttest

class TestDefiningFunctionsCall(asttest.ASTTest):

    def setUp(self):
        super().setUp("login.py")

    def test_values(self):
        self.assertIn("NAME", self.file, "Do not remove the NAME variable from"
                " your solution.")
        self.assertIn("DNUMBER", self.file, "Do not remove the DNUMBER "
                "variable from your solution.")
        from login import NAME, DNUMBER
        if len(NAME)<3:
            self.fail("You did not enter your name correctly.")
        if len(DNUMBER)!=9 or (len(DNUMBER)==9 and DNUMBER[0]!="D" and not DNUMBER[1:].isdecimal()):
            self.fail("You did not enter you D# correctly.")

if __name__ == "__main__":
    unittest.main()
