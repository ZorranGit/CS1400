from cisc108 import assert_equal
def make_receipt(x):
    discpri=x*.9
    print (x)
    print (discpri)
    return discpri

make_receipt(make_receipt(20))
