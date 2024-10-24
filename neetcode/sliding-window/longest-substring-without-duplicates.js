// URL - https://neetcode.io/problems/longest-substring-without-duplicates

class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const charSet = new Set();
        let left = 0;
        let result = 0;

        for (let r = 0; r < s.length; r++) {
            const char = s[r]
            if (charSet.has(char)) {
                while (charSet.has(char)) {
                    charSet.delete(s[left]);
                    left++;
                }
            }

            charSet.add(char)
            result = Math.max(charSet.size, result)
        }

        return result;
    }
}

const s = new Solution()
let str = "dvdf"
str = "zxyzxyz"

console.log(s.lengthOfLongestSubstring(str))

