// URL - https://neetcode.io/problems/min-cost-climbing-stairs

class Solution {
  /**
   * @param {number[]} cost
   * @return {number}
   */
  minCostClimbingStairs(cost) {
    const dp = (i) => {
      if (i >= cost.length) {
        return 0;
      }

      const currentCost = cost[i];
      return Math.min(dp(++i) + currentCost, dp(++i) + currentCost);
    }

    return Math.min(dp(0), dp(1));
  }
}


const s = new Solution();
const cost =  [1,2,1,2,1,1,1];

console.log(s.minCostClimbingStairs(cost));