# 692. 前K个高频单词
# https://leetcode-cn.com/problems/top-k-frequent-words/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_num = defaultdict(int)
        for word in words:
            word_num[word] += 1
        word_num = sorted(word_num.items(),key=lambda d:(-d[1],d[0]))
        # print(word_num)
        ans = []
        for i in range(k) :
            ans.append(word_num[i][0])
        return ans