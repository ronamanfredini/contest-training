
function frequencyOfMaxValue(numbers, q) {
  let rightToLeftAnswer = []

  let currentMax = Number.MIN_SAFE_INTEGER
  let currentMaxCount = 0

  for (let i = numbers.length - 1; i >= 0; i--) {
    if (numbers[i] > currentMax) {
      currentMax = numbers[i]
      currentMaxCount = 0
    }

    if (numbers[i] == currentMax) {
      currentMaxCount++
    }

    rightToLeftAnswer[i] = currentMaxCount
  }

  return q.map(idx => rightToLeftAnswer[idx - 1])
}

console.log(frequencyOfMaxValue([5,4,5,3,2], [1,2,3,4,5]))