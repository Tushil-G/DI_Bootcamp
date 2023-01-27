let ans= prompt("Type several words (separated by commas).")
let word=ans.split(",")


 let lengthOfword=getlength()
 showrow()
 function showrow(){
 const Rowfirst= firstrow()

 console.log(Rowfirst);
 for (const words of word){showword(words)}

 console.log(Rowfirst)}
 function showword(words){
    let empty=" ".repeat(lengthOfword-words.length)
    console.log("* "+words+empty+" *")
     }

 function getlength(){
     let lengthOfword=0
     for (let words of word){
         let wordlength=words.length;
         if (wordlength>lengthOfword){lengthOfword=wordlength}
      
     }
     return lengthOfword
     }


 function firstrow(){
     let noOfStars=lengthOfword+4;
     let row=""
     for (let i=0;i<noOfStars;i++){
         row= row+"*"
     }
     return row
 }
