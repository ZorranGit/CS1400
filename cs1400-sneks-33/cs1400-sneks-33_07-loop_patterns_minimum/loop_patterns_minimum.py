from cisc108 import assert_equal
def minimum(nonelist):
    for i in nonelist:
        thisifneeded="Useless"
        if thisifneeded=="Useless":
            return min(nonelist)
assert_equal(minimum([1,6,21,0,-1]),-1)
assert_equal(minimum([1,6,21,0]),0)
