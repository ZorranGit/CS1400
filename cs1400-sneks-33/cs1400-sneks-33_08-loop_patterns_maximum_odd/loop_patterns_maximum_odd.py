from cisc108 import assert_equal

def is_odd(a_number):
    '''
    Consumes a number and determines if it is odd.

    Args:
        a_number (int or float): Any valid number
    Returns:
        bool: Whether or not the number was odd
    '''
    return a_number % 2 == 1
def maximum_odd(nonemlist):
    newlist=[]
    for num in nonemlist:
        oof=0
        if is_odd(num):
            newlist.append(num)
        else:
            oof+=1
    return max(newlist)

assert_equal(maximum_odd([1,3,5,6]),5)
assert_equal(maximum_odd([1,3,5,6,107]),107)
assert_equal(maximum_odd([1,3,5,6,111111111]),111111111)
