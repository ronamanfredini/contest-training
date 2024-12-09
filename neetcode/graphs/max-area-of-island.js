// URL - https://neetcode.io/problems/max-area-of-island
class Solution {
  memo = new Map();

  /**
   * @param {number} i
   * @param {number} j
   * @param {number[][]} grid
   * @return {number}
   */
  dfs(i, j, grid) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length) {
      return 0;
    }

    const value = grid[i][j];

    if (value === 0) {
      return 0;
    }
    
    const coordinate = `${i}${j}`;
    if (this.memo.has(coordinate)) {
      return 0;
    }

    this.memo.set(coordinate, true);

    return this.dfs(i + 1, j, grid) 
            + this.dfs(i - 1, j, grid)
            + this.dfs(i, j + 1, grid)
            + this.dfs(i, j - 1, grid) + 1;
  }

  /**
   * @param {number[][]} grid
   * @return {number}
   */
  maxAreaOfIsland(grid) {
    let maxSize = 0;
    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
        maxSize = Math.max(maxSize, this.dfs(i, j, grid));
      }
    }

    return maxSize;
  }
}

const s = new Solution();
const grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

console.log(s.maxAreaOfIsland(grid))