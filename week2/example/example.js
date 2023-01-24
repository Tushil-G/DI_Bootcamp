let addressNumber="5"
let addressStreet="Benyenhuda"
let country="Israel"
console.log("I live in" + " "+ addressStreet+" "+ addressNumber+", in"+ " "+ country)
let animal=['cat','dog','fish','rabbit','cow']
console.log(animal[1])
animal.push("horse")
console.log(animal)
animal.splice(3,1)
console.log(animal)
////////////////////////
console.log("ex 2")
let lang=prompt("ENG/FREN/HIB") 

switch (lang) {
  case 'ENG':
    console.log('Hello');
    break;
  case 'FREN':
    console.log('bonjour')
    break
  case 'HIB':
    console.log('shalom');
    break;

}