len=int(input("how many nos do you want to store"))
list1=[]
for num in range(0,len):
    val=int(input("enter a value"))
    if val>=100:
        list1.append("over")
    else:
        list1.append(val)
print(list1)
            
