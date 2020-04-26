// Complete the minimumBribes function below.
function minimumBribes(q) {
    let bribed = [];
    let totalBribes = 0;
    for (let i = 0; i < q.length; i++) {
        if (q[i] > i + 1) {
            let timesBribed = q[i] - i - 1;
            if (timesBribed > 2) {
                console.log('Too chaotic');
                return;
            }
            bribed.push({initialPos: q[i], timesBribed: timesBribed, finalPos: i + 1});
            totalBribes += timesBribed;
        }
    }
    console.log(totalBribes);
}
5 - 2
7 - 2
8 - 1
6 -1
minimumBribes([1,2,5,3,7,8,6,4]);
                1,2,3,4,5,6,7,8