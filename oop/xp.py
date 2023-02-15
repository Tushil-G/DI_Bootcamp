# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age


# cat=Cat("lechat",15)
# cat1=Cat("kitten",2)
# cat2=Cat("thing",20)
# cats=[cat,cat1,cat2]


# def old_cat(cats):
#     old_cat=cats[0]
#     for old in cats:
#         if old.age > old_cat.age:
#             old_cat=old
#             return old_cat
# name=old_cat(cats).name
# age=old_cat(cats).age  
# print(f'The oldest cat name is {name} and its age is {age}')
# #ex 2
# class Dog:
#     def __init__(self,name,height):
#         self.name=name
#         self.height=height
    

#     def bark(self):
#         print(f'{self.name} is barking: "Woof woof"')

    
#     def high(self):
#         print(f"it's height is {self.height}cm and it can jump {self.height*2}cm")

# davids_dog=Dog("Rex",50)
# print(davids_dog.name)
# print(davids_dog.height)


# davids_dog.bark()
# davids_dog.high()

# sarah_dog = Dog("Teacup", 20)

# print(sarah_dog.name, sarah_dog.height)

# sarah_dog.bark()
# sarah_dog.high()

# list_of_dogs = [davids_dog, sarah_dog]


# def bigger_dog(list_of_dogs):
#     bigger_dog = list_of_dogs[0]
#     for dog in list_of_dogs:
#         if dog.height > bigger_dog.height:
#             bigger_dog = dog
#     return bigger_dog
# print(f"\n{bigger_dog(list_of_dogs).name} is the biggest dog")

#ex3
class song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for song in self.lyrics:
            print(song)
stairway= song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#4
class Zoo:
    def __init__(self, zoo_name):
        self.animal = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animal:
            self.animal.append(new_animal)

    def get_animals(self):
        print("The animals in the zoo:")
        for animal in self.animal:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animal:
            self.animal.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animal:
            if animal[0] not in sorted_animals:
                sorted_animals[animal[0]] = [animal]
            else:
                sorted_animals[animal[0]].append(animal)
        sorted_animals = dict(sorted(sorted_animals.items()))
        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        for key, value in sorted_animals.items():
            print(f"{key}: {value}")

my_zoo = Zoo("Ramat Gan Safari")
my_zoo.add_animal("Ape")
my_zoo.add_animal("Baboon")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Cat")
my_zoo.add_animal("Cougar")
my_zoo.add_animal("Eel")
my_zoo.add_animal("Emu")
my_zoo.get_animals()
my_zoo.sell_animal("Bear")
my_zoo.get_animals()
my_zoo.get_groups()
        





       