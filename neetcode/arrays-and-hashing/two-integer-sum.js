// URL - https://neetcode.io/problems/two-integer-sum
class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const resultMap = new Map();
        for (let i = 0; i < nums.length; i++) {
            const currentNumber = nums[i];
            const howMuchIsNeededInOrderToReturnTrue = target - currentNumber;

            if (resultMap.has(currentNumber)) {
                return [resultMap.get(currentNumber), i];
            }

            resultMap.set(howMuchIsNeededInOrderToReturnTrue, i);
        }
    }
}

// const nums = [3,4,5,6]
// const target = 7

// const solution = new Solution();
// console.log(solution.twoSum(nums, target));

