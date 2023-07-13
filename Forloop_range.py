#Adding even numbbers
list = input("Please input no's: ").split(",")

even_no =0
for i in list:
    if int(i)%2==0:
        even_no+=int(i)
print(even_no)