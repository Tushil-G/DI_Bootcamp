num=int(input("enter number: "))
len=int(input("enter length: "))
for i in range(len):
   i+=1
   print(f'{i}x{num}={num*i}')
# part 2
string=input("Enter string: ")
p=""
for char in string:
    if char not in p:
        p=p+char
print(p)#removes all duplicates
y=''
for x in string:
    if y=='' or x != y [ len(y)-1]:
     y=y+x
print(y)#removes all duplicates

