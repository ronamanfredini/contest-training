// URL - https://neetcode.io/problems/combination-target-sum
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target
   * @returns {number[][]}
   */
  combinationSum(nums, target) {
      const combinations = [];
      const triedCombinations = new Map();
      const dfs = (i = 0, combination = [], total = 0) => {
        if (total === target) {
            combinations.push([...combination]);
            return
        }
        if (total > target || i >= nums.length) {
            return;
        }

        combination.push(nums[i]);
        dfs(i, combination, total + nums[i]);
        combination.pop();
        dfs(i + 1, combination, total);
      }

      dfs()

      return Array.from(combinations.values());
  }
}

const s = new Solution();
const nums = [2,5,6,9], target = 9
console.log(s.combinationSum(nums, target))