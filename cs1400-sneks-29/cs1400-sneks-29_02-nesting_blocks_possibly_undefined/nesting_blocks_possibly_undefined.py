from cisc108 import assert_equal
def calculate_income(salary):
    if salary>5000:
        tax= .9
        return salary * tax
    else:
        return salary
assert_equal(calculate_income(1000), 1000)
assert_equal(calculate_income(10000), 9000.0)
