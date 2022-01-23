from cisc108 import assert_equal
def lookup_temperature(temps):
    temp=temps
    if temp  < 32:
        tempwrd="Freezing"
    elif temp >= 32 and temp < 50:
        tempwrd="Cold"
    elif temp >= 50 and temp < 70:
        tempwrd="Warm"
    elif temp >= 70:
        tempwrd="Hot"
    return tempwrd

assert_equal(lookup_temperature(50),"Warm")
assert_equal(lookup_temperature(70),"Hot")
assert_equal(lookup_temperature(40),"Cold")
assert_equal(lookup_temperature(20),"Freezing")
