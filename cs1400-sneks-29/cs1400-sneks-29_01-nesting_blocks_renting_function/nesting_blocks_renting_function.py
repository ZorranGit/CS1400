from cisc108 import assert_equal
def can_rent(age, has_license):
    if age < 1000:
        if age >= 21:
            if has_license:
                return ("Can rent a car")
            else:
                return ("Doesn't have a license")
        else:
            return ("Too young")
    else:
        return ("Too old")
assert_equal((can_rent(21,True)),("Can rent a car"))
assert_equal((can_rent(19,True)),("Too young"))
assert_equal((can_rent(25,False)),("Doesn't have a license"))
assert_equal((can_rent(9999,True)),("Too old"))
