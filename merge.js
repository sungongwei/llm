const fs = require('fs');
const base ='datasetdir/'
const output ='data/'
fs.existsSync(output) &&fs.rmdirSync(output, { recursive: true })
fs.mkdirSync(output, { recursive: true })

fs.readdirSync(base).forEach((dir) => {
  fs.writeFileSync(output + 'dev.json', fs.readFileSync(base + dir + '/dev.json'),{flag:'a+'}) 
  fs.writeFileSync(output + 'train.json', fs.readFileSync(base + dir + '/train.json'),{flag:'a+'}) 

})