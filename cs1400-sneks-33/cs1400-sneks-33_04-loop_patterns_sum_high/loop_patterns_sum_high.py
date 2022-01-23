from cisc108 import assert_equal
def sum_high(numlist):
    total=0
    for num in numlist:
        if num > 50:
            total+=num
        else:
            total+=0
    return total

assert_equal(sum_high([1,2,3,4,50,41,52,53]),105)
assert_equal(sum_high([1,2,3,4,50,41,52,59]),111)
