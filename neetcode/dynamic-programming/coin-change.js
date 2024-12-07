// URL - https://neetcode.io/problems/coin-change

class Solution {
  memo = new Map();
  /**
   * @param {number[]} coins
   * @param {number} amount
   * @return {number}
   */
  dfs(coins, amount) {
    if (amount === 0) {
      return 0;
    }

    if (this.memo.has(amount)) {
      return this.memo.get(amount);
    }

    let result = Number.MAX_SAFE_INTEGER;
    for (const coin of coins) {
      if (amount - coin >= 0) {
        result = Math.min(result, this.dfs(coins, amount - coin) + 1)
      }
    }

    this.memo.set(amount, result);
    return result;
  }

  /**
   * @param {number[]} coins
   * @param {number} amount
   * @return {number}
   */
  coinChange(coins, amount) {
    const result = this.dfs(coins, amount)

    if (result === Number.MAX_SAFE_INTEGER) {
      return -1;
    }

    return result;
  }
}


const s = new Solution();
const coins=[5,10, 1], amount=12
// const coins=[357,239,73,52], amount=9832
console.log(s.coinChange(coins, amount))