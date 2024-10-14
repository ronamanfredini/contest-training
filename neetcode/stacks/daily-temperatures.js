// URL - https://neetcode.io/problems/daily-temperatures

class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const tempMap = new Map();
        const result = new Array(temperatures.length).fill(0);

        for (let i = 0; i < temperatures.length; i++) {
            const temperature = temperatures[i];
            for (const [key, value] of tempMap.entries()) {
                const [idx, prevTemp] = key.split('_');
                if (temperature > parseInt(prevTemp)) {
                    tempMap.delete(key);
                    result[idx] = i - idx;
                }
            }
            
            
            const mapKey = `${i}_${temperature}`;
            tempMap.set(mapKey, 0);
        }

        return result;
    }
}

const temperatures = [30,38,30,36,35,40,28]
const s = new Solution()
console.log(s.dailyTemperatures(temperatures))