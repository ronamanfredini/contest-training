// URL - https://neetcode.io/problems/longest-repeating-substring-with-replacement

class Solution {
    getMostFrequentChar(map) {
        const mapEntries = Array.from(map.entries());

        if (mapEntries.length === 0) {
            return [null, 0];
        }

        let max = mapEntries[0][1];
        let mostFrequentChar = mapEntries[0][0];
        
        for (let i = 1; i < mapEntries.length; i++) {
            const [char, count] = mapEntries[i]
            if (count > max) {
                mostFrequentChar = char;
                max = count
            }
        }

        return [mostFrequentChar, max];
    }

    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const charMap = new Map();
        let l = 0;
        let maxLength = 0;
        let maxf = 0

        for (let r = 0; r < s.length; r++) {
            const char = s[r];
            let windowLength = r - l + 1;
            const currentCharCount = (charMap.get(char) || 0) + 1;
            charMap.set(char, currentCharCount);

            maxf = Math.max(maxf, currentCharCount);

            while (windowLength - maxf > k) {
                const lChar = s[l];
                const lCharCount = charMap.get(lChar) - 1;
                charMap.set(lChar, lCharCount)
                l++;
                windowLength = r - l + 1;
            }

            maxLength = Math.max(maxLength, windowLength);
        }

        return maxLength
    }
}


const s = "AAABABB", k = 1

const sol = new Solution()
console.log(sol.characterReplacement(s, k));