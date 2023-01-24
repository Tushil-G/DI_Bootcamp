const sentence=("This dinner is not that bad ! You cook well")
const wordNot= sentence.search("not")
const wordBad= sentence.search("bad")
if (wordNot==-1){console.log(sentence)}
else if (wordNot < wordBad){
const p1=sentence.slice(0,wordNot)
const p2=sentence.slice(wordBad+3)
console.log(p1+ "good" +p2)


}
else{console.log(sentence)}


