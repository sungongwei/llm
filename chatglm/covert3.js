const readline = require('readline');
const fs = require('fs');
const list = require('../out.json')

list.forEach(item => {
  fs.writeFileSync(`dev.json`, JSON.stringify({
    "conversations":
      [
        {
          "role": "user",
          "content": item.list[0]
        },
        {
          "role": "assistant",
          "content":item.answer
        }
      ]
  }) +'\n', { flag: "a+" })
  // if (item.list.length !== 1) {
  //     item.list.shift()
  // }
  item.list.forEach(question => {
    fs.writeFileSync(`train.json`, JSON.stringify({
      "conversations":
        [
          {
            "role": "user",
            "content": question
          },
          {
            "role": "assistant",
            "content":item.answer
          }
        ]
    })+'\n', { flag: "a+" })
  })


})
console.log(list)