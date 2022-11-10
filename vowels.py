elem=input("enter a word")
vowels=['a','e','i','o','u']
listb=[]
for x in elem:
    if(x in vowels and x not in listb):
        listb.append(x)
        print("vowels present in given string:",listb)
