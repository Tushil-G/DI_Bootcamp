#excercise 1
print("hello world "*3,"i love python "*3)

#excercise 2
month=int(input("enter month in num: "))
if month in (range(0,12)):
    print("~~correct month has been choosen~~")
if month==1:
    print("jan")
if month==2:
    print("feb")
if month==3:
    print("march")    
if month==4:
    print("april")
if month==5:
    print("may")
if month==6:
    print("june")
if month==7:
    print("july")
if month==8:
    print("august")
if month==9:
    print("sept")
if month==10:
    print("Oct")
if month==11:
    print("nov")
if month==12:
    print("dec")    
if month==3 and month<6:
    print("the season of the month is spring")
if month==6 and month<9:
    print("the season of the month is summer")
if month==9 and month<11:
    print("the season of the month is Autum")
if month==11 and month==12 and month==1 and month==2 and month==3:
    print("the season of the month is winter")
elif month>12:
    print("Nah bruh their's only 12 months")


