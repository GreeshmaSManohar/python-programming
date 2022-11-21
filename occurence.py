def word_count(str):
          count=dict()
          words=str.split()
          for word in words:
                    if word in count:
                        count[word]+=1
                    else:  
                         count[words]=1
          print(countt)
a=input("enter the string")
word_count(a)
