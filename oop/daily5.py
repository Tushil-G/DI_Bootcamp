from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

##this represents a class's objects as a string
    def __repr__(self):
        return "(%s,%s)" %(self.value, self.suit)#converts obj to string


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        for i in self.cards:
            print(i)

    def __repr__(self):
        return "Cards remaining in deck: {}".format(len(self.cards))
    
    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
            return self.cards
        else:
            return("Only full decks can be shuffled")
            

    def deal(self):
        if len(self.cards) != 0:
            return self.cards.pop()
        else:
            return("All cards have been dealt")
            
            

d=Deck()
print("Deck created")

print("\nShuffling the deck\n")
x=d.shuffle()
for i in x:
    print(i)
a=int(input("\nEnter 1 to deal the cards \n"))

while(a==1):
    print(d.deal())
    print(d)
    a=int(input("Enter 1 to deal the cards (or) any key to discontinue \n"))
print(d.shuffle())


#part 1 
# What is a class?it is a outline to create object
# What is an instance?An object 
# What is encapsulation?wrapping data and methods that work on data within one unit
# What is abstraction?A process of handling complex things by hiding unnecessary information from the user
# What is inheritance?A class that allows all methods to inherit proprties from another class
# What is multiple inheritance?A class that derives from multiple/more than one base class
# What is polymorphism?A method in child class that have the same name as the method of parent class
# What is method resolution order or MRO?A hierarchy of classes

