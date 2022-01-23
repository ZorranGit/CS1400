names=open("names.txt")
for i in names:
    i=i.split(",")
    name=i[1].capitalize()
    name=name.strip("\n")
    lastname=i[0].capitalize()
    print(name, lastname)
names.close()
