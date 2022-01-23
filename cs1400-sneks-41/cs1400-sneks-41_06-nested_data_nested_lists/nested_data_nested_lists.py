hourly_donations_per_day = [
    [44, 33, 56, 27, 33, 25],
    [12, 15, 22, 19, 21],
    [36, 34, 32, 37, 28, 11, 35],
    [20, 19, 29],
    [22, 27, 21, 15, 26, 15]
    ]
total=0
count=0
for donolist in hourly_donations_per_day:
 #   num=int((donolist[0]))
    fine=0
    for i in donolist:
        fine+=i
    count+=1
    total+=fine
print(total)
