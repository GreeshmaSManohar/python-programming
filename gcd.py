num1=int(input("enter a num"))
num2=int(input("enter a num"))
gcd=1
for i in range(1,min(num1,num2)):
     if(num1%i==0)and(num2%i==0):
         gcd=i
print("gcd of",num1,"and",num2,"is",gcd)         
         
