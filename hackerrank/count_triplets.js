let geometricProgressionMemory = [];
function searchGPTriplet(arr, startIndex, progressionCount, progressionRate) {
    if (progressionCount >= 3) return true;
    let startedProgressionNumber = arr[startIndex];

    if (geometricProgressionMemory[startedProgressionNumber]) {
        return searchGPTriplet(arr, geometricProgressionMemory[startedProgressionNumber][1], ++progressionCount, progressionRate);
    }

    let searchingFor = startedProgressionNumber * progressionRate;
    for (let i = startIndex + 1; i < arr.length; i++) {
        if (arr[i] == searchingFor) {
            geometricProgressionMemory[startedProgressionNumber] = [searchingFor, i];
            return searchGPTriplet(arr, i, ++progressionCount, progressionRate);
        }
        if (arr[i] > searchingFor) break;
    }
    return false;
}


function countTriplets(arr, r) {
    let tripletCount = 0;
    for (let i = 0; i < arr.length; i++) {
        tripletCount += searchGPTriplet(arr, i, 1, r)? 1: 0;
    }

    return tripletCount;
}

console.log(countTriplets([1,2,2,4], 2));
