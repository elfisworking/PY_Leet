# 208. 实现 Trie (前缀树)
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/
# 应用场景：关键词提示功能、IDE的自动补全功能等等
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._children = [None]*26
        self._is_end_char = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for index,char in map(lambda x:(ord(x)-ord('a'),x),word):
            if not root._children[index]:
                root._children[index]=Trie()
            root = root._children[index]
        root._is_end_char = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        for index in map(lambda x:ord(x)-ord('a'),word):
            if not root._children[index]:
                return False
            root = root._children[index]
        return root._is_end_char


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self
        for index in map(lambda x:ord(x)-ord("a"),prefix):
            if not root._children[index]:
                return False
            root = root._children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)