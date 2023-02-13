class Farm:
    def __init__(self, names):
        self.name = names
        self.animals = {}

    def animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def info(self):
        animal_types = self.animals.keys()
        output = f"{self.name}'s farm\n"
        for animal_type in animal_types:
            count = self.animals[animal_type]
            output += f"{animal_type} : {count}\n"
        output += "\n    E-I-E-I-0!"
        return output

    def animal_types(self):
        return sorted(self.animals.keys())

    def get_info(self):
        animal_types = self.animal_types()
        animal_string =", ".join(animal_types)
        return f"{self.name}'s has a lot of {animal_string}."


macdonald = Farm("McDonald")
macdonald.animal("cow", 5)
macdonald.animal("sheep")
macdonald.animal("sheep")
macdonald.animal("goat", 12)
print(macdonald.info())
print(macdonald.get_info())