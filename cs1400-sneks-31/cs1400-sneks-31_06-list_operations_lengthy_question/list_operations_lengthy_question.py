from cisc108 import assert_equal
def check_length(listboi):
    if len(listboi)>=3 and len(listboi)<=5:
        return True
    else:
        return False
assert_equal((check_length([1,2,3,4,5,6])),False)
assert_equal((check_length([1,2,3,4,5])),True)
