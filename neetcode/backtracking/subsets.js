// URL - https://neetcode.io/problems/subsets

class Solution {
  /**
   * @param {number[]} nums
   * @return {number[][]}
   */
  subsets(nums) {
    const result = [];
    const subset = [];
    const aux = (idx) => {
      if (idx >= nums.length) {
        result.push([...subset])
        return;
      }
      
      subset.push(nums[idx])
      aux(idx + 1)
      subset.pop()
      aux(idx + 1)
    }

    aux(0)

    return result
  }
}

const s = new Solution();

console.log(s.subsets([1, 2, 3]))