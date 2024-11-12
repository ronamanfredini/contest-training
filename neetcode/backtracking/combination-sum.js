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
      const combinations = new Map();
      const triedCombinations = new Map();
      const aux = (combination) => {
          combination = combination.sort();
          const key = combination.join();
          if (triedCombinations.has(key)) {
              return
          }
          triedCombinations.set(key, combination);

          const sum = combination.reduce((curr, acc) => curr + acc, 0);
          if (sum > target) {
              return;
          }

          if (sum === target) {
              combinations.set(key, combination);
              return
          }

          for (const num of nums) {
              aux([...combination, num]);
          }
      }

      aux([])

      return Array.from(combinations.values());
  }
}
