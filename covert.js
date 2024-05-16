const readline = require('readline');
const fs = require('fs');
const list = []
let last = ''
fs.readFileSync('a.txt', { encoding: 'utf-8' }).split('\n').forEach(line => {
  let [title, answer] = line.split('\t')
  answer = answer.replace(/\b/g, '')
  if (!answer) {
    answer =last
  } 
  last= answer
  list.push({title,answer})
})
fs.writeFileSync('a.json', JSON.stringify(list))
// list.forEach(item => {
//   fs.writeFileSync(`dev.json`, JSON.stringify({
//     "conversations":
//       [
//         {
//           "role": "user",
//           "content": item.list[0]
//         },
//         {
//           "role": "assistant",
//           "content":item.answer
//         }
//       ]
//   }) +'\n', { flag: "a+" })
//   // if (item.list.length !== 1) {
//   //     item.list.shift()
//   // }
//   item.list.forEach(question => {
//     fs.writeFileSync(`train.json`, JSON.stringify({
//       "conversations":
//         [
//           {
//             "role": "user",
//             "content": question
//           },
//           {
//             "role": "assistant",
//             "content":item.answer
//           }
//         ]
//     })+'\n', { flag: "a+" })
//   })


// })
// console.log(list)