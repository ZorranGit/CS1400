from lib.midterm import *
from login import *
generate(NAME, DNUMBER)
# DO NOT CHANGE ANYTHING ABOVE THIS LINE
# WRITE YOUR SOLUTION BELOW THIS LINE
def is_surrounded(sentence):
    return(sentence.startswith("[") and sentence.endswith("]"))

print(is_surrounded("[Lets see]"))
