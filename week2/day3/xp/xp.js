// // const people = ["Greg", "Mary", "Devon", "James"];
// // people.shift();
// // people.splice(2,3,"Jason")
// // people.push("Tushil")
// // console.log(people.indexOf("Mary"))
// // console.log(people);
// // let array;
// // array=(people.slice(1,3))
// // console.log(array)
// // console.log("if it's -1 Foo is not in array= "+people.indexOf("Foo"))
// // let last;
// // last=array.lastIndexOf("Jason")
// // console.log(last+" -- will be last")
// // for(let i=0;i<people.length;i++){console.log(people[i])
// //     if (people[i] === 'Jason') {break;}

// //     }
// // //excercise 2
// // let colours=['blue','red','green','yellow','light blue']

// // for (let i = 0; i < 5; i++) {console.log("My "+"#"+i+ " choice "+colours[i])
// //     if(colours[i]==='light blue'){break}}
// // ///excercise 3
// // let s=(prompt("Enter num"))
// // while (s< 10) {s=prompt("Number should be higher")}
// ///excercise 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors)
console.log("Number of apartments available: " + building.numberOfAptByFloor['firstFloor']+" , "+building.numberOfAptByFloor['thirdFloor'])
console.log("Second tenant: "+building.nameOfTenants[1]+" , "+" number of rooms: "+building.numberOfRoomsAndRent['dan'][0])
if (building.numberOfRoomsAndRent['sarah'][1]+building.numberOfRoomsAndRent['david'][1]>1000){building.numberOfRoomsAndRent['dan'][1]=1200}
console.log(building.numberOfRoomsAndRent)
// // ///excercise 5
// // let family = {firstname:['sam','bob','ted']};
// // for (let x in family) {
// //   console.log(x) 
// //   console.log(family[x]) 
// // }
// //excercise 6
// // const details = {
// //     my: 'name',
// //     is: 'Rudolf',
// //     the: 'raindeer'
// //   }
// //   let x=''
// //   for (let sentence in details){x=x+ sentence+" "+details[sentence]+" ";}
// //     console.log(x)
// ////Excercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let If=names.map(x => x.toUpperCase())
let letter=If.map(y=> y.charAt())
let sort=letter.sort()
let secret=sort.join("")
console.log(secret)





 
   



