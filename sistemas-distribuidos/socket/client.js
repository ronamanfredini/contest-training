//CLIENT
const who = 'CLIENT'
const readline = require("readline");
const connection = require('./handlers/connection')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question("De qual base você quer fazer backup?", async (answer) => {
  const response = await connection.doRequest(8070, {
    message: answer,
    origin: who
  })

  console.log(response)
})

