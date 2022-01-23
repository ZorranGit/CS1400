from cisc108 import assert_equal

person1 = {"Name": "Charles Babbage", "Age": 17}
person2 = {"Name": "Ada Lovelace", "Age": 32}

def make_older(person):
    person["Age"] += 1
    return person["Age"]

assert_equal(make_older(person1), 18)
assert_equal(person1, {"Name": "Charles Babbage", "Age": 18})
assert_equal(make_older(person2), 33)
assert_equal(person2, {"Name": "Ada Lovelace","Age": 33})
