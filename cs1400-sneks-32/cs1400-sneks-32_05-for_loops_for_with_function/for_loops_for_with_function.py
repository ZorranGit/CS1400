def convert_fahrenheit(celtemp):
    fahrenheit = celtemp *9/5+32
    return fahrenheit

templist=[10,20,30]
for i in templist:
    print(convert_fahrenheit(i))
