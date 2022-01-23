from cisc108 import assert_equal

def extract_key(animalboi, keyboi):
    count=0
    new=[]
    for i in animalboi:
        new.append(animalboi[count][keyboi])
        count+=1
    return new

animals = [
    {"Name": "Klaus", "Weight": 27, "Height": 18},
    {"Name": "Pumpkin", "Weight": 20, "Height": 16},
    {"Name": "Wrex", "Weight": 3, "Height": 2},
]
animals2 = [
    {"Name": "Klaus", "Weight": 27, "Height": 18},
    {"Name": "Pumpkin", "Weight": 20, "Height": 16},
    {"Name": "Wrex", "Weight": 3, "Height": 2},
    {"Name": "Don", "Weight": 4, "Height": 3}
]
assert_equal(extract_key(animals, "Height"), [18, 16, 2])
assert_equal(extract_key(animals2, "Height"), [18, 16, 2, 3])
