// URL - https://neetcode.io/problems/three-integer-sum

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const ascSortingFunc = (a, b) => a - b
        const sortedNums = nums.sort(ascSortingFunc);
        const solutions = new Map();

        for (let i = 0; i < sortedNums.length; i++) {
            const target = sortedNums[i] * -1;

            for (let l = 0, r = sortedNums.length - 1; l < r;) {
                const sum = sortedNums[l] + sortedNums[r];

                if (l === i) {
                    l++;
                    continue
                }

                if (r === i) {
                    r--;
                    continue;
                }

                if (sum === target) {
                    const solution = [sortedNums[i], sortedNums[l], sortedNums[r]];
                    const solutionKey = solution.sort(ascSortingFunc)
                                                .reduce(
                                                    (acc, current) => acc.toString() + current.toString(), 
                                                    ''
                                                );
                    solutions.set(solutionKey, solution);
                    l++;
                    r--;
                    continue;
                }

                if (sum > target) {
                    r--;
                    continue;
                }

                if (sum < target) {
                    l++;
                    continue;
                }
            }
        }

        return Array.from(solutions.values())
    }
}


const nums = [-1,0,1,2,-1,-4];

const solution = new Solution();

console.log(solution.threeSum(nums));