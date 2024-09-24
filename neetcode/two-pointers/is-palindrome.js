// URL - https://neetcode.io/problems/is-palindrome
class Solution {
    isAlpha(char) {
        let charCode = char.charCodeAt(0);
        if (!(charCode > 47 && charCode < 58) &&  !(charCode > 96 && charCode < 123) && !(charCode > 64 && charCode < 91)
        ) {
           return false;
        }

        return true;
    }

    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const onlyLetters = s.toLowerCase();

        for (let s = 0, f = onlyLetters.length - 1; s < f;) {
            let startLetter = onlyLetters[s];
            let endLetter = onlyLetters[f];

            while (!this.isAlpha(startLetter) && s < f) {
                startLetter = onlyLetters[++s];
            }

            while (!this.isAlpha(endLetter) && f > s) {
                endLetter = onlyLetters[--f];
            }

            if (startLetter !== endLetter) {
                return false;
            }

            s++;
            f--;
        }

        return true;
    }
}

const solution = new Solution();
const s = "tab a cat";
console.log(solution.isPalindrome(s))