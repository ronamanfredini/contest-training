// URL - https://neetcode.io/problems/longest-consecutive

class Solution {
    /**
     * @param {Map<number, Array<number>} currentSublistMap
     * @param {number} num
     * @param {number[]} currentSubList
     * @return {number[]}
     */    
    handleConflict(currentSublistMap, num, currentSublist) {
        const nextSubList = currentSublistMap.get(num);
        if (!nextSubList) {
            return currentSublist;
        }

        currentSublist = Array.from(new Set([...currentSublist, ...nextSubList]));
        currentSublistMap.delete(num);

        const nextNumberToCheck = num + 1;
        if (currentSublistMap.has(nextNumberToCheck)) {
            return this.handleConflict(currentSublistMap, nextNumberToCheck, currentSublist)
        }

        return currentSublist;
    }

    /**
     * @param {Map<number, Array<number>} currentSublistMap
     * @param {number} num
     * @return {null}
     */
    handleNextList(currentSublistMap, num) {
        let currentSublist = currentSublistMap.get(num);
        currentSublistMap.delete(num)
        currentSublist.push(num);
        currentSublist = this.handleConflict(currentSublistMap, num + 2, currentSublist);

        const nextNeededNumber = currentSublist[currentSublist.length - 1] + 1;
        currentSublistMap.set(nextNeededNumber, currentSublist);
    }

    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const sublistMap = new Map();
        let longestSublist = 0;

        for (const num of nums) {
            if (!sublistMap.has(num)) {
                sublistMap.set(num + 1, [num]);
                continue;
            }

            this.handleNextList(sublistMap, num);
        }

        for (const list of sublistMap.values()) {
            longestSublist = Math.max(longestSublist, list.length);
        }

        return longestSublist;
    }
}


const solution = new Solution();

const nums = 
// [2,20,4,10,3,4,5];
[0,3,2,5,4,6,1,1]
console.log(solution.longestConsecutive(nums));