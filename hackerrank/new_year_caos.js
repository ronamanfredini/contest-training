function minimumBribes(q) {
	let bribesCount = 0;
	for (let i = 0; i < q.length; i++) {
		let initialPosition = q[i] - 1;

		let positionsAhead = initialPosition - i;
		if (initialPosition > 0) {
			bribesCount += positionsAhead; 
		}
		if (positionsAhead > 2) {
			console.log("Too chaotic");
		}
	}
	console.log(bribesCount);
}

minimumBribes([1, 2 ,5 ,3, 4, 7, 8, 6]);