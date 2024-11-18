// URL - https://neetcode.io/problems/climbing-stairs

class Solution {
  /**
   * @param {number} n
   * @return {number}
   */
  climbStairs(n, memo = new Map()) {
      if (n <= 0) {
          return 0;
      }

      if (n === 1) {
          return 1;
      }

      if (n === 2) {
          return 2
      }

      if (memo.has(n)) {
        return memo.get(n);
      }

      const left = this.climbStairs(--n, memo);
      memo.set(n, left);
      const right = this.climbStairs(--n, memo);
      memo.set(n, right);

      return left + right;
  }
}
