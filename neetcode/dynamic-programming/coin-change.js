// URL - https://neetcode.io/problems/coin-change

class Solution {
  /**
   * @param {number[]} coins
   * @param {number} amount
   * @return {number}
   */
  dfs(coins, amount, coinCountSoFar = 0) {
    if (amount === 0) {
      return coinCountSoFar;
    }

    if (coins.length === 0) {
      return -1;
    }

    const coin = coins.pop();
    if (coin > amount) {
      return this.dfs(coins, amount, coinCountSoFar);;
    }

    const reminder = amount % coin;
    coinCountSoFar += Math.floor(amount / coin);

    return this.dfs(coins, reminder, coinCountSoFar);
  }
  /**
   * @param {number[]} coins
   * @param {number} amount
   * @return {number}
   */
  coinChange(coins, amount) {
    if (amount === 0) {
      return 0;
    }

    coins = coins.sort((a, b) => a - b);
    while (coins.length > 0) {
      const result = this.dfs(coins, amount);
      if (result > 0) {
        return result;
      }
      coins.pop();
    }

    return -1;
  }
}


const s = new Solution();
const coins=[11, 22, 33, 44, 55, 66, 77, 88, 99, 111], amount=330
console.log(s.coinChange(coins, amount))