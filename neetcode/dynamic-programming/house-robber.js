// URL - https://neetcode.io/problems/house-robber


class Solution {
  /**
   * @param {number[]} nums
   * @return {number}
   */
  rob(nums) {
    nums.push(0)
    let i = nums.length - 4
    for (; i >= 0; i-=2) {
      nums[i] = Math.max(nums[i] + nums[i + 2]);
      nums[i + 1] = Math.max(nums[i + 1] + nums[i + 3]);
    }

    if (i === -1) {
      nums[0] = Math.max(nums[0] + nums[2]);
    }

    return Math.max(nums[0], nums[0 + 1]);
  }
}

const s = new Solution();
const cost =  [1,1, 3, 3];

console.log(s.rob(cost));