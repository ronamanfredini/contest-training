function rotLeft(a, d) {
	let firstElementIndex = d % (a.length);
	let resultArr = new Array();
	for (let i = firstElementIndex; i < a.length; i++) {
		resultArr.push(a[i]);
	}
	for (let i = 0; i < firstElementIndex; i++) {
		resultArr.push(a[i]);
	}
	return resultArr;
}

rotLeft([1,2,3,4,5], 4);