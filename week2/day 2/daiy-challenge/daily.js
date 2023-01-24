let sentence='This movie is not that bad !'
let word=sentence.indexOf('not')
let notword=sentence.indexOf('bad')
if(word>0){sentence=sentence.replace("not that","good")
,sentence=sentence.replace("bad","")}
else if (word=-1){sentence}
console.log(sentence)

