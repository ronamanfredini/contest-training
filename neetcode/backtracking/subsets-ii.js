// URL - https://neetcode.io/problems/subsets-ii

class Solution {
  /**
   * @param {number[]} nums
   * @return {number[][]}
   */
  subsetsWithDup(nums) {
    const result = new Map();
    const dfs = (i, currentResult = []) => {
      if (i >= nums.length) {
        const newCurrentResult = [...currentResult];
        const key = newCurrentResult.sort().join('');
        result.set(key, newCurrentResult);
        return;
      }

      const num = nums[i];
      currentResult.push(num);
      dfs(i + 1, currentResult);
      currentResult.pop();
      dfs(i + 1, currentResult);
    };

    dfs(0);

    return Array.from(result.values());
  }
}

const s = new Solution();
const nums = [1,2,1]
console.log(s.subsetsWithDup(nums))