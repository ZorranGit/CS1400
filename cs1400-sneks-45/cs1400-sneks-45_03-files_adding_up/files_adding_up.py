rainfall=open("rainfall.txt")
total_rainfall=0
for i in rainfall:
    total_rainfall+=float(i)
print(total_rainfall)
rainfall.close()
