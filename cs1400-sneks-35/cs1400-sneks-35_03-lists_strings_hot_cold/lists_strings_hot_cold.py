from cisc108 import assert_equal
def add_hot_cold(obvstr):
    total=0
    count=0
    for i in obvstr:
        if obvstr[count]=="H":
            total+=1
        else:
            total-=1
        count+=1
    return total
assert_equal(add_hot_cold("CHCC"),-2)
assert_equal(add_hot_cold("HHCC"),-0)
