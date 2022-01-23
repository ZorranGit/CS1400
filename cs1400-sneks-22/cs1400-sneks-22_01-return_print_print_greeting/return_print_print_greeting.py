from cisc108 import assert_equal
def print_greeting(name):
    print("Hello " + name)

print_greeting("Donavan")
assert_equal(print_greeting("Donavan"), None)
