// URL - https://neetcode.io/problems/anagram-groups
class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagramsLists = new Map();

        for (const str of strs) {
            const letterCount = new Map();
            for (const letter of str) {
                let currentLetterCount = letterCount.get(letter) || 0;

                letterCount.set(letter, ++currentLetterCount);
            }

            const letterCountKeys = Array.from(letterCount.keys()).sort();
            let hashKey = '';
            for (const key of letterCountKeys) {
                const howManyCharactersWereFoundWithThisLetter = letterCount.get(key);
                hashKey += `${key}${howManyCharactersWereFoundWithThisLetter}`;
            }

            const currentList = anagramsLists.get(hashKey) || [];
            currentList.push(str);
            anagramsLists.set(hashKey, currentList);
        }

        const result = Array.from(anagramsLists.values());
        return result;
    }
}

// const solution = new Solution();

// const strs = ["act","pots","tops","cat","stop","hat"];
// // const strs = ["pots","tops"];
// console.log(solution.groupAnagrams(strs))
