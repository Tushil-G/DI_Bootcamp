msg=input("Enter something.... ")
if len(msg)<10 :
    print("more letters plz")
if len(msg)>20:
    print("too long")
for i in range(len(msg)):
    print(msg[i])