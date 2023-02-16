# class Computer():

#     def __init__(self):
#         self.name = "Apple Computer" # public
#         self.__max_price = 900 # private

#     def sell(self):            # public method
#         print(f"Selling Price: {self.__max_price}")

#     def __sell(self):          # private method
#       print('This is private method')

#     def set_max_price(self, price):
#         self.__max_price = price
# c = Computer()
# print(c.name)
# c.sell()
# list_1 = [ 'asdada', 1, 123131.131, 'blaa adaraerada', 0.000001, 34.12451235265, 'stackoverflow is awesome' ]
# list_2 = [num for num in list_1 if isinstance(num, (str))]#print only only string()
# print(list_2)
from faker import Faker
fake = Faker()

# Writing fake names to the file
with open('output.txt', 'w') as f:
    for i in range(10):
       f.write(f'{fake.name()}\n')

# Reading from the file jsut created
for line in open('output.txt'):
    print(line)