// URL - https://neetcode.io/problems/top-k-elements-in-list

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const numCountMap = new Map();

        for (const number of nums) {
            let countOfNumOnMap = numCountMap.get(number) || 0;
            numCountMap.set(number, ++countOfNumOnMap);
        }

        const sorted = Array.from(numCountMap.entries()).sort((a, b) => {
            const aCounter = a[1];
            const bCounter = b[1];

            return bCounter - aCounter;
        })

        const kEntries = [];

        for (let i = 0; i < k; i++) {
            const [sortedKey] = sorted[i]
            kEntries.push(sortedKey)
        }

        return kEntries;
    }
}


const solution = new Solution();

// const nums = [1,2]
// const k = 2

const nums = [1,2,2,3,3,3]
const k = 2

console.log(solution.topKFrequent(nums, k))