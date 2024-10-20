// URL - https://neetcode.io/problems/eating-bananas

class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        const sortedPiles = piles.sort();
        const allBananas = piles.reduce((a, b) => a + b, 0);
        let minRatio = 1

        
        while (true) {
            minRatio = Math.max(Math.ceil(allBananas / h), minRatio)
            let hoursPassed = 0
            const pileCopy = [...sortedPiles];

            while (pileCopy.length > 0) {
                if (hoursPassed > h) {
                    minRatio++;
                    break;
                }

                hoursPassed += Math.ceil(pileCopy[pileCopy.length - 1] / minRatio);
                pileCopy.pop();
            }

            if (pileCopy.length === 0 && hoursPassed <= h) {
                return minRatio;
            }

            minRatio++;
        }
    }
}


const s = new Solution();

const piles = [25,10,23,4], h = 4

console.log(s.minEatingSpeed(piles, h))