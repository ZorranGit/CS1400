from cisc108 import assert_equal
def filter_high(numlist):
    newlist=[]
    for i in numlist:
        if i <= 50:
            newlist.append(i)
        else:
            behappy=0
    return(newlist)
assert_equal(filter_high([1,2,3,50,24,59]),[1,2,3,50,24])
assert_equal(filter_high([1,2,3,50,24,59,52]),[1,2,3,50,24])
