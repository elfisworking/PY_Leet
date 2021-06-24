# 剑指 Offer 13. 机器人的运动范围
# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
# 跟12题很相似，直接套就行了
class Solution:
    # 感觉又是一个DFS
    def movingCount(self, m: int, n: int, k: int) -> int:
        def add(row,col):
            res = 0
            while row!=0:
                res += row%10
                row = row//10
            while col!= 0:
                res += col%10
                col = col//10
            return res
        def check(i,j):
            if len(visited) == m*n:
                return 
            visited.add((i,j))
            if add(i,j) <= k:
                res[0] += 1
                for idx,idy in directions:
                    newidx ,newidy = i+idx,j+idy
                    if 0<=newidx<m and  0 <= newidy < n:
                        if (newidx,newidy) not in visited:
                            check(newidx,newidy)
            pass
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = [0]
        check(0,0)
        return res[0]
