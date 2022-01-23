from cisc108 import assert_equal

def return_greeting(name):
    return("Hello " + name)

return_greeting("Donavan")
assert_equal(return_greeting("Donavan"), "Hello Donavan")
