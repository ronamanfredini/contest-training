class Solution {
  // Method to calculate the minimum number of operations to reduce the array
  reductionOperations(nums) {
    nums.sort((a, b) => a - b);
    let operationCount = 0;

    let i = nums.length - 1;
    let rightMostNumber = nums[i];

    while (i >= 0) {
      if (rightMostNumber !== nums[i]) {
        const charToReplace = nums[i];
        i++;
        while (i < nums.length) {
          operationCount++;
          nums[i] = charToReplace;
          i++;
        }
        rightMostNumber = charToReplace;
      }

      i--;
    }

    return operationCount;
  }
}


const s = new Solution();
const test = [100, 50, 50, 25];
console.log(s.reductionOperations(test))
