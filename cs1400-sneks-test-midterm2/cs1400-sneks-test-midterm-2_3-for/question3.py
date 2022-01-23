def count_me(listboi,value):
    total=0
    count=0
    for i in listboi:
        if listboi[count] == value:
            total+=1
        else:
            pass
        count+=1
    return(total)
print(count_me(["Dream","Dream","Dream","Potato","Dream"],"Potato"))
