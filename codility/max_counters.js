function solution(N, A) {
    let counters = Array(N);
    counters.fill(0);

    let maxCounter = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] <= N) {
            counters[A[i] - 1]++;
            if (counters[A[i] - 1] > maxCounter) {
                maxCounter = counters[A[i] - 1];
            }
        } else {
            let tempCounters = Array(N);
            tempCounters.fill(maxCounter);
            counters = tempCounters;
        }
    }
    return counters;
}
