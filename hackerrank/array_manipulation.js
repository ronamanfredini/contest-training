function arrayManipulation(n, queries) {
	let arr = [];
	let maxValue = Number.MIN_SAFE_INTEGER;
	arr.length = n;
	arr.fill(BigInt(0));

	for (let i = 0; i < queries.length; i++) {
		for (let j = queries[i][0]; j <= queries[i][1]; j++) {
			arr[j - 1] += BigInt(queries[i][2]);
			if (arr[j - 1] > maxValue) {
				maxValue = arr[j -1];
			}
		}
	}
	return maxValue.toString().substr(0, maxValue.length);
}

console.log(arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]]));