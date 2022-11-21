flist=[]
slist=[]
sum1=0
sum2=0
len1=int(input("how many numbers do you want to add n  first list/"))
for i in range(0,len1):
               inp1=int(input("enter the value for element"))
               flist.append(inp1)
len2=int(input("enter the value for the elemenadd in second list?t"))
for i in range (0,len2):
    inp2=int(input("enter the value of element"))
    slist.append(inp2)


if(len(flist)==len(slist)):
     print("two list are of same length")

for num1 in flist:
    sum1+=num1

for num2 in slist:
    sum2+=num2

if sum1==sum2:
     print("the sum of values of element in both flist are equal")
else:
     print("the sum of values of both list elements are different")


for num in flist:
  if num in slist:
     print(num,"found in both list \n")
