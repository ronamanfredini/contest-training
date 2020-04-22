function hourglassSum(arr) {
	let maxHourglassSum = Number.MIN_SAFE_INTEGER;
	for (let i = 0; i < arr.length; i++) {
		if (undefined == arr[i + 1] || undefined == arr[i + 2])
			break;
		for (let j = 0; j < arr[i].length - 2; j++) {
			if (arr[i][j + 1] == undefined || arr[i][j + 2] == undefined)
				break; 
			let hourglassSum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
											arr[i + 1][j + 1] +
								arr[i + 2][j] + arr[2 + i][j + 1] + arr[2 + i][j + 2];
			if (hourglassSum > maxHourglassSum) {
				maxHourglassSum = hourglassSum;
			}
		}
	}
	return maxHourglassSum;
}

console.log(hourglassSum([[1, 1, 1, 0, 0, 0],
						[0, 1, 0, 0, 0, 0],
						[1, 1, 1, 0, 0, 0],
						[0, 0, 2, 4, 4, 0],
						[0, 0, 0, 2, 0, 0],
						[0, 0, 1, 2, 4, 0],
					]))