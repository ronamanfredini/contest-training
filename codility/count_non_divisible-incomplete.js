function solution(A) {
	A.sort((a,b) => a - b);
	let aux = [];
	let parsedNumbers = [];

	for (let i = 0; i < A.length; i++) {
		if (A[i] != 0) {
			if (parsedNumbers[A[i]]) {

			} else {
				let posSqrt = parseInt(Math.floor(Math.sqrt(A[i])));
				for (let j = A[i]; A[i] < posSqrt; j--) {
					if (A[i] % j > 0) {
						if (!aux[j]) {
							aux[j] = [];
						}
						aux[j].push(A[i]);
					}
				}
			}
		}
	}
}


console.log(solution([3,1,2,3,6]));
