const  _ = require("lodash")
const  fs = require("fs")

const output ='data/'

_.shuffle(fs.readFileSync(output + 'dev.json',{encoding:'utf8'}).split('\n')).forEach((line) => {
  fs.writeFileSync(output + 'dev_shuffled.json', line+'\n',{flag:'a+'}) 
})
_.shuffle(fs.readFileSync(output + 'train.json',{encoding:'utf8'}).split('\n')).forEach((line) => {
  fs.writeFileSync(output + 'train_shuffled.json', line+'\n',{flag:'a+'}) 
})
