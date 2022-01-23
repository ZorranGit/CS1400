from cisc108 import assert_equal
def convert_operator(stringboi):
    if stringboi=="+":
        return 1
    elif stringboi=="-":
        return -1
    else:
        return 0
plusminus=open("plus_and_minus.txt")
total=0
for i in plusminus:
    for k in i:
        ok=convert_operator(k)
        total+=ok
    print(total)
assert_equal(convert_operator("-"), -1)
assert_equal(convert_operator("+"), 1)
