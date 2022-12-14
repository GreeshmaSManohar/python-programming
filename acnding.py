import operator
d={1:2,3:4,3:2,8:9}
print("orginal dictionary:",d)
sort_d=sorted(d.items(),key =operator.itemgetter(1))
print("dictionary in ascending order by value:",sort_d)
sort_d=dict(sorted(d.items(),key=operator.iteamgetter(1),reverse=True))
print("dictionary in descending order by value:",sort_d)
