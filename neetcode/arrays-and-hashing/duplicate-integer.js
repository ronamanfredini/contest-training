// URL: https://neetcode.io/problems/duplicate-integer
class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numMap = new Map();

        for (const num of nums) {
            if (numMap.has(num)) {
                return true;
            }
            numMap.set(num, true)
        }

        return false;
    }
}
