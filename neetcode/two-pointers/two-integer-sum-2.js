// URL - https://neetcode.io/problems/two-integer-sum-ii

class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
       for (let l = 0, r = numbers.length - 1; l < r;) {
            const sum = numbers[l] + numbers[r];

            if (sum === target) {
                return [l + 1, r + 1];
            }

            if (sum > target) {
                r--;
                continue;
            }

            if (sum < target) {
                l++;
                continue;
            }
       } 
    }
}


const solution = new Solution();
const numbers = [1,2,3,4], target = 3;

console.log(solution.twoSum(numbers, target));