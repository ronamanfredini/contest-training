// URL - https://neetcode.io/problems/products-of-array-discluding-self

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let accumulator = 1;
        let zeroCount = 0;
        const result = [];


        for (const num of nums) {
            if (num === 0) {
                zeroCount++;
                if (zeroCount > 1) {
                    return new Array(nums.length).fill(0);
                }

                continue;
            }

            accumulator = accumulator * num;
        }

        for (const num of nums) {
            if (num === 0) {
                result.push(accumulator);
                continue
            }

            if (zeroCount === 1) {
                result.push(0);
                continue;
            }

            result.push(accumulator / num);
        }

        return result;
    }
}


const solution = new Solution();
const nums = [-1,0,1,2,3]
console.log(solution.productExceptSelf(nums))