let favorite_food="Chocolate"
let favorite_meal="dinner"
console.log("I eat " +" "+ favorite_food+" at every "+ favorite_meal)
//excercise 2
console.log("part 1:")
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries
console.log("I watched 3 series : "+myWatchedSeriesLength)
//part 2
console.log("part 2:")
const myWatchedSeries1 = ["black mirror", "money heist", "the big bang theory"];
myWatchedSeries1.splice(2,2,"Friends")
console.log(myWatchedSeries1)
//excercise 3
let temperature = prompt("Temperature:")
let x= (temperature/5)*9+32
console.log(x+" in temperature°F.")
//excercise 4
let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:55,34 plus 21 is 55
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction:23, a has a new value(2),so by adding 2 with 21,23 will be the answer
    // Actual:23
    
    //excercise 5
    typeof(15)
// Prediction:Integer(a numerical type)
// Actual:number

typeof(5.5)
// Prediction:float(Becausse it has decimal point)
// Actual:float

typeof(NaN)
// Prediction:NaN
// Actual:

typeof("hello")
// Prediction:string<because every characters inside"" are string
// Actual:string

typeof(true)
// Prediction:Boolean(true/false)
// Actual:BOolean

typeof(1 != 2)
// Prediction:True (1 is not equal to 2)
// Actual:

"hamburger" + "s"
// Prediction:hamburgers,s is being added to "hamburger"
// Actual:hamburgers

"hamburgers" - "s"

// Prediction:Null(substraction cannot be perform)
// Actual:NaN

"1" + "3"
// Prediction:4(1 plus 3)
// Actual:4

"1" - "3"

// Prediction:-2 (1 minus 3)
// Actual:-2

"johnny" + 5
// Prediction:jhonny5
// Actual:

"johnny" - 5
// Prediction:NaN(substration cannot be perform)
// Actual:

99 * "hello"
// Prediction:Error/NaN(it cannot be perform)
// Actual:NAn

1 != 1
// Prediction:False
// Actual:False

1 == "1"
// Prediction:True(1 id equal to 1)
// Actual:True

1 === "1"
// Prediction:False(1 is not a integer(it is assign as string))
// Actual:False
