let geometricProgressionMemory = [];
function searchGPTriplet(arr, startIndex, progressionCount, progressionRate, multiplier) {
    if (progressionCount >= 3) return multiplier;
	startIndex = parseInt(startIndex);
	let startedProgressionNumber = arr[startIndex];

    if (geometricProgressionMemory[startedProgressionNumber]) {
        return searchGPTriplet(arr, geometricProgressionMemory[startedProgressionNumber][1], ++progressionCount, progressionRate, multiplier * geometricProgressionMemory[startedProgressionNumber][1].length);
    }

    let searchingFor = startedProgressionNumber * progressionRate;
    for (let i = startIndex + 1; i < arr.length; i++) {
        if (arr[i] == searchingFor) {
			geometricProgressionMemory[startedProgressionNumber] = [searchingFor, [i]];
			for (let j = i + 1; arr[j] == searchingFor; j++) {
				geometricProgressionMemory[startedProgressionNumber][1].push(j);
			}
			
            return searchGPTriplet(arr, i, ++progressionCount, progressionRate, geometricProgressionMemory[startedProgressionNumber][1].length * multiplier);
        }
        if (arr[i] > searchingFor) break;
    }
    return 0;
}

function countTriplets(arr, r) {
	let tripletCount = 0;
	arr.sort((a,b) => a > b);
    for (let i = 0; i < arr.length; i++) {
        tripletCount += searchGPTriplet(arr, i, 1, r, 1);
    }

    return tripletCount;
}

console.log(countTriplets([1,3,9,9,27,81], 3));
