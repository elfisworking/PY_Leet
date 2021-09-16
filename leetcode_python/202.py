from collections import defaultdict
from typing import List
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.word = ""
    
    def insert(self,word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(now,i,j):
            if board[i][j] not in now.children:
                return 
            
            ch = board[i][j]
            now = now.children[ch]

            if now.word != "":
                ans.add(now.word)
            
            board[i][j] = "#"
            for a , b in [(i+1 ,j), (i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= a < m and 0 <= b < n:
                    dfs(now,a,b)
            board[i][j] = ch

        ans = set()
        m, n = len(board) , len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie,i,j)
        
        return list(ans)
