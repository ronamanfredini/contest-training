// URL - https://neetcode.io/problems/max-water-container

class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;
        for (let l = 0, r = heights.length - 1; l < r;) {
            const leftColumn = heights[l];
            const rightColumn = heights[r];
            const currentArea = Math.min(leftColumn, rightColumn) * (r - l);

            maxArea = Math.max(maxArea, currentArea);

            if (leftColumn < rightColumn) {
                l++;
                continue;
            }

            if (rightColumn < leftColumn) {
                r--;
                continue;
            }

            l++;
        }

        return maxArea;
    }
}

const solution = new Solution();

const heights = [1,7,2,5,4,7,3,6];
console.log(solution.maxArea(heights));
