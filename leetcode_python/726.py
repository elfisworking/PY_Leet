# 726. 原子的数量
# https://leetcode-cn.com/problems/number-of-atoms/
class Solution:
    def __init__(self):
        self.i = 0
    def countOfAtoms(self, formula: str) -> str:
        l = len(formula)
        stack = [defaultdict(int)]
        def parse_aton():
            s =  [formula[self.i]]
            self.i += 1
            nonlocal l
            while self.i < l and formula[self.i].islower():
                s.append(formula[self.i])
                self.i += 1
            return "".join(s)
        def parse_num():
            nonlocal l
            if self.i == l or not formula[self.i].isdigit():
                return 1
            count = 0
            while self.i < l and formula[self.i].isdigit():
                count = 10*count + int(formula[self.i])
                self.i += 1
            return count
        while self.i < l:
            if formula[self.i] == "(":
                self.i += 1
                stack.append(defaultdict(int))
            elif formula[self.i] == ")":
                self.i += 1
                num = parse_num()
                popMap = stack.pop()
                topMap = stack[-1]
                for ch , v in popMap.items():
                    topMap[ch] += num * v
            else:
                ch = parse_aton()
                num = parse_num()
                topMap = stack[-1]
                topMap[ch] += num    
        topMap = stack[-1]
        ans = []
        topMap = sorted(topMap.items(),key = lambda x : x[0])
        for i in topMap:
            ans.append(i[0])
            if i[1] > 1:
                ans.append(str(i[1]))
        return "".join(ans)