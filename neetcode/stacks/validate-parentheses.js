// URL - https://neetcode.io/problems/validate-parentheses

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const opposingCharacters = new Map([
            // ['{', '}'],
            // ['[', ']'],
            // ['(', ')'],
            [')', '('],
            [']', '['],
            ['}', '{'],
        ])
        const stack = [];
        if (s.length % 2 !== 0) {
            return false;
        }

        for (const char of s) {
            const stackTop = stack[stack.length - 1];
            console.log(stack)
            if (stackTop === opposingCharacters.get(char)) {
                stack.pop();
            } else {
                stack.push(char);
            }
        }

        return stack.length === 0;
    }
}


const solution = new Solution();
const s =  "([])";
console.log(solution.isValid(s))