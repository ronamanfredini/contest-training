// URL - https://neetcode.io/problems/k-closest-points-to-origin

class Solution {
  calculateDistance(x1, y1) {
    const x2 = 0;
    const y2 = 0;
    return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2))
  }

  /**
   * @param {number[][]} points
   * @param {number} k
   * @return {number[][]}
   */
  kClosest(points, k) {

  }
}

const s = new Solution();
console.log(s.calculateDistance(0, 2))