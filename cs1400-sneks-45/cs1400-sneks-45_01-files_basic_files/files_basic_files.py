test=open("grocery_list.txt")

for i in test:
    i=i.strip("\n")
    print(i)


test.close()
