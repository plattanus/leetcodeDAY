from typing import Deque, List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for char in word:
                idx = ord(char) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.isEnd = True
        
        self.root.fail = self.root
        q = Deque()
        for i in range(26):
            if self.root.children[i]:
                self.root.children[i].fail = self.root
                q.append(self.root.children[i])
            else:
                self.root.children[i] = self.root
        while q:
            node = q.popleft()
            node.isEnd = node.isEnd or node.fail.isEnd
            for i in range(26):
                if node.children[i]:
                    node.children[i].fail = node.fail.children[i]
                    q.append(node.children[i])
                else:
                    node.children[i] = node.fail.children[i]

        self.temp = self.root
            
    def query(self, letter: str) -> bool:
        self.temp = self.temp.children[ord(letter) - ord('a')]
        return self.temp.isEnd

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.fail = None

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


