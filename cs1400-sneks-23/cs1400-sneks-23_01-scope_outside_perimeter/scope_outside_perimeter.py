from cisc108 import assert_equal

def calculate_perimeter(width, height):
    perimeter = width *2 + height * 2
    return perimeter
assert_equal(calculate_perimeter(4, 3), 14)
