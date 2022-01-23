from cisc108 import assert_equal
def add_positives(num1,num2):
    if num1>0 and num2>0:
        return(num1+num2)
    else:
        return 0
assert_equal(add_positives(1,2),3)
assert_equal(add_positives(0,2),0)
