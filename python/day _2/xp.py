# #exercise 1
# my_fav_numbers={18,19,20,21,22}
# my_fav_numbers.add(23)
# my_fav_numbers.add(24)
# #excercise 2
# my_fav_numbers=set(list(my_fav_numbers)[:-1])#my_fav_numbers.remove(24)
# fr_numbers={25,36,77,90}
# our=fr_numbers.union(my_fav_numbers)
# print(our)
# #if combine last digit must be remove our=set(list(our)[:-1])

# #excercise 2
# #Given a tuple which value is integers, is it possible to add more integers to the tuple?no
# #excercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("kiwi")
# basket.insert(0,"Apples")
# print(f' the amount of apples are: {basket.count("Apples")}')
# basket.clear()
# print(basket)
# #excercise 4
# #What is a float? What is the difference between an integer and a float?float have decimal value for instance 1.3
# # #Can you think of another way to generate a sequence of floats?yes
# my_list=[1]
# num=0
# while num<8:
#     my_list.append(my_list[-1]+0.5)
#     num+=1
# print(my_list)
#excecise 5
# for x in range(1,20):
#     print(x+1)
# for x in range(1,21):
#     if (x % 2) == 0:
#         print(f'these numbers are even {x}')

 #excercise 6
# nom=""
# while nom !="tushil":
#     nom=input("enter name plz: ")
#     nom=nom.lower()
# else:
#     print("you finally remebered your name")
# excercise 7

# fav_fruit=input("what is your favorite fruit {plz add a space between each fruit}: ")
# fruit=fav_fruit.split()
# print(fruit)
# fruit=input("fruit choice: ")
# if fruit in fav_fruit:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# excercise 8
# top=0
# while True:
    
#     topping=input("What do you want as topping//type quit to quit: ")
#     top+=1
#     if topping=="quit":
#         x=top*2.5
#         print("Total price for pizza is: ",(x-2.5)+10)
#         break

# #sentence=input("input: ")#time challenge 2
# #re=' '.join(sentence.split()[::-1])
# #print(re)
#time challenge 1
# x=int(input("is_this number a perfect number: "))
# s=0
# for i in range(1,x):
#     if x%i==0:
#         s=s+i    
# if x==s:
#     print("True")
# else:
#  print("False")

#excercise 9
#if age <3
#output(0)
#if age>3 and  <12
#output(10)
#if age>13
#output(15)
#input age
#total=ticket+total
#     ex    #
# age=-1
# price=[]
# while age!=0:
#     age=int(input("what is your age"))
#     if age<=3:
#         price.append(0)
#     elif age<3 and age>=12:
#         price.append(10)
#     elif age>12:
#         price.append(15)
#     elif age==0:
#         break
# print(f"Total price: {sum(price)}")
# teenagers=int(input("how many people are their? "))
# nameAllow=[]
# for i in range(teenagers):
#   name=input("what is your name: ")
#   Age=int(input("what is your age? ".format(name)))
#   if Age>=16 and Age<=21:
#     nameAllow.append(name)
# print("Final list ",nameAllow)
# excercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich" ,"Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches =[]
for i in sandwich_orders:
    finished_sandwiches.append(sandwich_orders)
    print(f'i made your {i}')
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    for x in sandwich_orders:
     print(f'we have your {x}')#let it run at least 3 times
    
print("we ran out of pastrami sandwi")






   
     

     
               










