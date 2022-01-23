from cisc108 import assert_equal
from string import ascii_letters
def starts_with_letter(word):
    while word[0] in ascii_letters:
        return True
    else:
        return False
assert_equal(starts_with_letter("Test"),True)
assert_equal(starts_with_letter("&est"),False)
