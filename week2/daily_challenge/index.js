const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.pop(0)
fruits.sort()
fruits.push("Kiwi")
const removeApple = fruits.slice(1)

removeApple.reverse()
console.log(removeApple)
//Excercise 2
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0])