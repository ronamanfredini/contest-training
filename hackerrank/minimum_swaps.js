
// Complete the minimumSwaps function below.
function minimumSwaps(arr) {

    let swapCount = 0;
    for (let i = 0 ; i < arr.length; i++) {
        if (i + 1 != arr[i]) {
            for (let j = i + 1; j < arr.length; j++) {
                if (i + 1 == arr[j]) {
                    let temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                    swapCount++;
                    break;
                }
            }
        }
    }
    return swapCount;
}


console.log(minimumSwaps([7,1,3,2,4,5,6]));