'use strict';

const fs = require('fs');
const https = require('https');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Complete the 'getRelevantFoodOutlets' function below.
 *
 * URL for cut and paste
 * https://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>
 *
 * The function is expected to return an array of strings.
 * 
 * The function accepts a city argument (String) and maxCost argument(Integer).
 */

const axios = require('axios')

async function doRequest(city, page) {
  return await axios.get(`https://jsonmock.hackerrank.com/api/food_outlets?city=${city}&page=${page}`)
}

async function getAllPages(city) {
  const firstRequest = await doRequest(city, 1)
  let data = [...firstRequest.data.data]
  if (firstRequest.data.total_pages > 1) {
    for (let i = 2; i <= firstRequest.data.total_pages; i++) {
      const response = await doRequest(city, i)
      data = [...data, ...response.data.data]
    }
  }

  return data
}

async function getRelevantFoodOutlets(city, maxCost) {
  const data = await getAllPages(city)
  const filtered = data.filter(item => item.estimated_cost <= maxCost)
  return filtered.map(item => item.name)
}


getRelevantFoodOutlets("Houston", 30).then(result => console.log(result))