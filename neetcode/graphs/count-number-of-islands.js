// URL - https://neetcode.io/problems/count-number-of-islands

class Solution {
  memo = new Set();

  /**
   * @param {number} i
   * @param {number} j
   * @param {character[][]} grid
   */
  ff(i, j, grid) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length) {
      return;
    }

    const coordinate = `${i}${j}`;
    if (this.memo.has(coordinate)) {
      return;
    }

    
    if (grid[i][j] === '0') {
      return;
    }

    this.memo.add(coordinate);
  
    this.ff(i + 1, j, grid);
    this.ff(i - 1, j, grid);
    this.ff(i, j + 1, grid);
    this.ff(i, j - 1, grid);
  }

  /**
   * @param {character[][]} grid
   * @return {number}
   */
  numIslands(grid) {
    let islandCount = 0;

    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
        const coordinate = `${i}${j}`;
        if (!this.memo.has(coordinate) && grid[i][j] === '1') {
          this.ff(i, j, grid);
          islandCount++;
        }
      }
    }


    return islandCount;
    
  }
}


const  grid = [
  ["1","1","0","0","1"],
  ["1","1","0","0","1"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

const s = new Solution();
console.log(s.numIslands(grid))