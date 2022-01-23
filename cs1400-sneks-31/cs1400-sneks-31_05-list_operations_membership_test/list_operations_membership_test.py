from cisc108 import assert_equal
def is_weekend(listthing):
    if "Saturday" in listthing or "Sunday" in listthing:
        return True
    else:
        return False

assert_equal(is_weekend(["Saturday", "Sunday", "Monday"]),True)
assert_equal(is_weekend(["Friday", "Tuesday", "Monday"]),False)
