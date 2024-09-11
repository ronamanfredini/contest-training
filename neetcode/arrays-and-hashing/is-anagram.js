// URL: https://neetcode.io/problems/is-anagram
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const mapS = new Map();
        const mapT = new Map();

        if (s.length !== t.length) {
            return false;
        }

        for (let i = 0; i < s.length; i++) {
            const sChar = s[i];
            const tChar = t[i];

            let mapSItem = mapS.get(sChar) || 0;
            let mapTItem = mapT.get(tChar) || 0;

            mapS.set(sChar, ++mapSItem);
            mapT.set(tChar, ++mapTItem);
        }

        for (const [key, mapSItem] of mapS) {
            if (!mapT.has(key)) {
                return false;
            }

            const mapTItem = mapT.get(key);

            if (mapTItem !== mapSItem) {
                return false;
            }
        }

        return true;
    }
}

// const solution = new Solution();

// console.log(solution.isAnagram('racecar', 'carrace'));
