// URL - https://neetcode.io/problems/permutations

class Solution {
  /**
   * @param {number[]} nums
   * @return {number[][]}
   */
  permute(nums) {
    const result = [];
    const dfs = (i = 0, combination = new Set()) => {
      if (combination.size === nums.length) {
        result.push([...combination]);
        return;
      }

      if (combination.size > nums.length || i >= nums.length) {
        return;
      }

      combination.add(nums[i]);
      dfs(i, combination);
      combination.delete(nums[i])
      dfs(i + 1, combination);
    };

    dfs();
    return result;
  }

}


const s = new Solution();
const nums = [1,2,3]
console.log(s.permute(nums))