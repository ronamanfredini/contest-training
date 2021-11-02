'use strict'

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