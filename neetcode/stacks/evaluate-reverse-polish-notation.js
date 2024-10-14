// URL - https://neetcode.io/problems/evaluate-reverse-polish-notation

class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []
        const operators = new Map([
            ['/', true],
            ['-', true],
            ['+', true],
            ['*', true],
        ])
        for (const char of tokens) {
            if (!operators.has(char)) {
                stack.push(parseInt(char));
            } else {
                const last = stack.pop();
                const first = stack.pop();
                let newItem = 0;

                if (char === '+') {
                    newItem = first + last;
                }

                if (char === '-') {
                    newItem = first - last;
                }

                if (char === '*') {
                    newItem = first * last;
                }

                if (char === '/') {
                    newItem = parseInt(first / last);
                }
                stack.push(newItem);
            }
        }
        return stack.pop()
    }
}


const tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
const solution = new Solution();
console.log(solution.evalRPN(tokens))