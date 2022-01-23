def maximum(listboi):
    highest_num=0
    if len(listboi) ==0:
        return None
    else:
        for number in listboi:
            if number > highest_num:
                highest_num = number
    return highest_num
print(maximum([1,5,6,8,9,7]))
