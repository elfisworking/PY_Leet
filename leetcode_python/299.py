# 299. 猜数字游戏
# https://leetcode-cn.com/problems/bulls-and-cows/
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dic =defaultdict(int)
        for index ,val in enumerate(secret):
            secret_dic[val] += 1
        bulls = 0 
        cows = 0
        pair_dic = defaultdict(int)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                secret_dic[guess[i]] -= 1
            else:
                pair_dic[guess[i]] += 1
        
        for ch , num in pair_dic.items():
            reminder = secret_dic[ch]
            cows += min(reminder,num)
        return str(bulls)+"A"+str(cows)+"B"
# 一开始又没有读懂题目
class Solution_2:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        return f'{bulls}A{cows}B'
