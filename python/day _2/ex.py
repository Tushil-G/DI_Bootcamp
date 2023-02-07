list1=[1,2,3,4,5,20,20,4]
replace=list1.index(20)
list1[replace]=200
#Replace first one
print(list1)
#replace all
str(list1)
replace1=[200 if item ==20 else item for  item in list1]
print(replace1)