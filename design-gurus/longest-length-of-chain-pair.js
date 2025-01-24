class Solution {
  // Function to find the maximum length of a pair chain
  findLongestChain(pairs) {
    // ToDo: Write Your Code Here.
    pairs.sort(([a, b], [c, d]) => {
      return b - c;
    });
    let chain = [];
    let longestChain = 0;
    let left = 0;
    let right = 0;

    for (let i = 0; i < pairs.length; i++) {
      const currentPair = pairs[i];
      if (chain.length === 0) {
        chain.push(currentPair);
        longestChain = Math.max(longestChain, chain.length);
        continue;
      }

      const chainLastNode = chain[chain.length - 1];
      if (chainLastNode[1] < currentPair[0]) {
        chain.push(currentPair);
      } else {
        chain = [currentPair];
      }
      longestChain = Math.max(longestChain, chain.length);
    }

    return longestChain;  // Return the maximum chain length
  }
}

const s = new Solution();
console.log(s.findLongestChain([[1,2], [2,3], [3,4], [4,5]]))
