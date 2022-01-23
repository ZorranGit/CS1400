from cisc108 import assert_equal
def get_name(dictboi):
    return dictboi["Name"]

assert_equal(get_name({"Name":"Donavan",
                      "Age": 2
                      }),"Donavan")
assert_equal(get_name({"Name":"Jim",
                      "Age": 2
                      }),"Jim")
