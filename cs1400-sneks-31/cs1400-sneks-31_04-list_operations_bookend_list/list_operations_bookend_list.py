from cisc108 import assert_equal
def bookend_list(list):
    newlist=[]
    if len(list)==0:
        return list
    else:
        newlist.append(list[0])
        newlist.append(list[-1])
        return newlist
assert_equal(bookend_list([1,2,3,4]),[1,4])
assert_equal(bookend_list([1,2,3,4,5,6,7,8]),[1,8])
assert_equal(bookend_list([.1,2,3,4,5,6,7,8]),[0.1,8])
assert_equal(bookend_list([]),[])
