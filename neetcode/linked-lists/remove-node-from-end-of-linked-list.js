// URL - https://neetcode.io/problems/remove-node-from-end-of-linked-list

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class ListNode {
  constructor(val = 0, next = null) {
      this.val = val;
      this.next = next;
  }
}

class Solution {
  /**
   * @param {ListNode} head
   * @param {number} n
   * @return {ListNode}
   */
  removeNthFromEnd(head, n) {
    const listMap = new Map();
    let counter = 0;
    while (head) {
      listMap.set(++counter, head);
      head = head.next;
    }

    if (listMap.size === 1) {
      return null;
    }
    const nodeIdxToRemove = 1 + listMap.size - n;

    if (nodeIdxToRemove === 1) {
      return listMap.get(2);
    }

    const prevNodeIdx = nodeIdxToRemove - 1;
    const nextNodeIdx = nodeIdxToRemove + 1;

    const prevNode = listMap.get(prevNodeIdx);
    const nextNode = listMap.get(nextNodeIdx) || null;
    const firstNode = listMap.get(1);

    prevNode.next = nextNode;

    return firstNode;
  }
}

let head = [1,2], n = 1

head = head.reverse().reduce((acc, curr) => new ListNode(curr, acc), null);

const s = new Solution();

console.log(s.removeNthFromEnd(head, n));
