from cisc108 import assert_equal
def cube_elements(numlist):
    newlist=[]
    for num in numlist:
        cubedboi= num*num*num
        newlist.append(cubedboi)
    return newlist

assert_equal(cube_elements([1,2,3,4,5]),[1,8,27,64,125])
assert_equal(cube_elements([2,4,5]),[8,64,125])
