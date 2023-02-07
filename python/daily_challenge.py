msg=input("Enter something.... ")
if len(msg)<10 :
    print("more letters plz")
if len(msg)>10:
    print("too long")
else:
    print(msg[0],msg[-1])
    x=" "
for y in msg:
    x+=y
    print(x)
    import random
shuffle="".join(random.sample(msg,len(msg)))
print(shuffle)