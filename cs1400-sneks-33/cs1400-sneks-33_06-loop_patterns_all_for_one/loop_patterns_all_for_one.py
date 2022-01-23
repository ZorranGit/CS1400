from cisc108 import assert_equal
def all_true(bollist):
    lol=0
    for bol in bollist:
        while bol==False:
            lol+=1
            break
    return (lol==0)

assert_equal(all_true([True,True,True,True]),True)
assert_equal(all_true([True,True,False,True]),False)
