// URL - https://neetcode.io/problems/permutations

class Solution {
  /**
   * @param {number[]} nums
   * @return {number[][]}
   */
  permute(nums) {
    const result = [];
    const dfs = (availableChoices = [], permutation = []) => {
      if (permutation.length === nums.length) {
        result.push([...permutation]);
        return;
      }

      for (let i = 0; i < availableChoices.length; i++) {
        const num = availableChoices[i];
        const newPermutation = [...permutation];
        newPermutation.push(num);
        const newAvailableChoices = [...availableChoices];
        newAvailableChoices.splice(i, 1);

        dfs(newAvailableChoices, newPermutation)
      }
    };

    dfs([...nums]);
    return result;
  }
}


const s = new Solution();
const nums = [1,2,3]
console.log(s.permute(nums))