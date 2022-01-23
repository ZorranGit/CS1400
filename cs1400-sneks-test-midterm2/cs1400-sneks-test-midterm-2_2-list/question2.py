def midpoint(listboi):
    for i in listboi:
        half=len(listboi)//2
        if len(listboi) % 2 != 0:
            half= (len(listboi))//2
        else:
            half= len(listboi)//2
        return listboi[half]

print(midpoint([1,5,6,True,"1",False,2]))
print(midpoint([0, 0, 1, 0, 0]))
