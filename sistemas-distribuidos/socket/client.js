//CLIENT
const fs = require('fs');
const who = 'CLIENT'
const readline = require("readline");
const dataHandler = require('./handlers/data')
const connection = require('./handlers/connection')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


async function ask() {
  rl.question("De qual base você quer fazer backup?\n", async (answer) => {
    try {
      const response = await connection.doRequest(8070, {
        message: answer,
        origin: who,
        type: 'data'
      })
      const formatted = dataHandler.formatData(dataHandler.formatData(response))
      if (formatted.status) {
        fs.writeFileSync(`./backups/base${answer}.json`, formatted.baseData)
        console.log(`[CLIENT] --> Base ${answer} successfully backuped`)
      } else {
        console.log(`[CLIENT] --> ${formatted.baseData}`)
      }

    } catch(err) {
      console.log('CLIENT ERROR -> ', err)
    }
    
    ask()
  })
}

ask()