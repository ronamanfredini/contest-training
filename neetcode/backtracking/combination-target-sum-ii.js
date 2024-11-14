// URL - https://neetcode.io/problems/combination-target-sum-ii

class Solution {
  /**
   * @param {number[]} candidates
   * @param {number} target
   * @return {number[][]}
   */
  combinationSum2(candidates, target) {
    const result = new Map();
    const dfs = (i = 0, sum = 0, chosenOnes = new Map()) => {
      if (sum === target) {
        const vals = Array.from(chosenOnes.values())
        const key = vals.sort().join('')
        result.set(key, vals);
        return;
      }
      if (chosenOnes.has(i) || sum > target || i >= candidates.length) {
        return;
      }


      chosenOnes.set(i, candidates[i] );
      dfs(i + 1, candidates[i] + sum, new Map(chosenOnes.entries()))
      chosenOnes.delete(i);
      dfs(i + 1, sum, new Map(chosenOnes.entries()))
    }

    dfs()

    return Array.from(result.values());
  }
}


const s = new Solution();
// const candidates = [1,2,3,4,5], target = 7
const candidates = [9,2,2,4,6,1,5], target = 8
console.log(s.combinationSum2(candidates, target))
