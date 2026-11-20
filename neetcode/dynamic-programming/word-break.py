from typing import List

class Solution:
    def build_trie(self, words):
        self.trie = {}
        for word in words:
            i = 0
            root = None
            for char in word:
                if i == 0:
                    root = self.trie.setdefault(char, {})
                else:
                    root = root.setdefault(char, {})
                i += 1
            root['*'] = True


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.build_trie(wordDict)
        self.memo = {}

        def find_words(i, root):
            char = s[i]
            if not root:
                root = self.trie.get(char)
            else:
                root = root.get(char)
            if not root:
                return False

            if i + 1 == len(s): 
                if root.get('*', False):
                    return True
                return False

            if not root:
                return False

            b1 = False
            if root.get('*', False):
                if i + 1 in self.memo:
                    return self.memo[i + 1]

                self.memo[i + 1] = find_words(i + 1, None)
                b1 = self.memo[i + 1]
                if b1:
                    return True

            b2 = find_words(i + 1, root)

            return b1 or b2
        return find_words(0, None)
            

        

def run_case(s: str, wordDict: List[str]) -> None:
    """Run wordBreak on s and wordDict and print the result."""
    print(f"s={s!r} wordDict={wordDict}")
    print(f"  got={Solution().wordBreak(s, wordDict)}")


# run_case("neetcode", ["neet", "code"])
# run_case("catsincars", ["cats", "cat", "sin", "in", "car"])
# run_case("aaaaaaa", ["aaaa", "aaa"])
run_case("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"])
