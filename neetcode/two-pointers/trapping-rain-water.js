// URL - https://neetcode.io/problems/trapping-rain-water

class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let waterCount = 0;
        let candidateWaterCount = 0;
        let maxHeight = 0;

        for (let i = 1; i < height.length; i++) {
            const currentHeight = height[i]

            if (currentHeight >= maxHeight) {
                waterCount += candidateWaterCount;
                candidateWaterCount = 0;
                maxHeight = currentHeight;
            }

            if (maxHeight === 0) {
                continue;
            }

            if (maxHeight === currentHeight) {
                continue;
            }

            candidateWaterCount += maxHeight - currentHeight;
        }

        return waterCount
    }
}


const solution = new Solution();

const height =  [0,2,0,3,1,0,1,3,2,1];

console.log(solution.trap(height))
