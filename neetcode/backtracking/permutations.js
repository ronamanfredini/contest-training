// URL - https://neetcode.io/problems/permutations

class Solution {
  /**
   * @param {number[]} nums
   * @return {number[][]}
   */
  permute(nums) {
    const result = [];
    const dfs = (i = 0, combination = []) => {
      if (combination.length === nums.length) {
        result.push([...combination]);
        return;
      }

      if (combination.length > nums.length || i >= nums.length) {
        return;
      }

      for (let j = 0; j < nums.length; j++) {
        const num = nums[j]
        if (j !== i) {
          combination.push(num);
          dfs(i + 1, combination)
          combination.pop()
        }
      }
      // combination.push(nums[i]);
      // dfs(i, combination);
      // combination.pop()
      // dfs(i + 1, combination);
    };

    dfs();
    return result;
  }

}


const s = new Solution();
const nums = [1,2,3]
console.log(s.permute(nums))