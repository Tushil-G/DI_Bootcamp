let count=prompt("Enter number plz")
let numberTakeDown=1
while (count>0){
    const num=loop(count,numberTakeDown);
    count=count-numberTakeDown
    numberTakeDown=numberTakeDown+1

    console.log(num)}
function loop(count,numberTakeDown){
    if(numberTakeDown>count-numberTakeDown){numberTakeDown=count}
let num=`We start the song ${count} at ${Bottle_bottles(count)}
-> Take _${numberTakeDown}_ down, pass ${them_it(count-numberTakeDown)} around
-> we have now ${count-numberTakeDown} ${Bottle_bottles(count-numberTakeDown)}`
return num}
function plural(count){if (count<2){
return true}
else{
    return false
}}
function Bottle_bottles(count){if (plural(count)){
    return "bottle"}
	else{

        return"bottles"}}
function them_it(count){if (plural(count)){
    return "it"}
    else{
        return "them"}
    }
      



                                            
