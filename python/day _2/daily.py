num=int(input("enter number: "))
lens=int(input("enter length: "))
list=[]
for i in range(lens):
   i+=1
   multiplication=(f'{i}x{num}={num*i}')
   list.append(multiplication)
print(list)
  

# # part 2
string=input("Enter string: ")
p=""
for char in string:
    if char not in p:
        p=p+char
print(p)#removes all duplicates
y=''
for x in string:
    if y=='' or x!= y [ len(y)-1]:
     y=y+x
print(y)#removes all duolicates/but not after another charater


