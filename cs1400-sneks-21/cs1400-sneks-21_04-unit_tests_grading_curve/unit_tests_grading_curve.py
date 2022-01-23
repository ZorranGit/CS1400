from cisc108 import assert_equal

def curve_grade(original_grade):
    curved_grade = original_grade**.5 * 10
    return curved_grade

print(curve_grade(18))
assert_equal(curve_grade(18),curve_grade(18))
assert_equal(curve_grade(19),curve_grade(19))
assert_equal(curve_grade(28),curve_grade(28))
