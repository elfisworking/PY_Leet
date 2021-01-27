from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        l = len(intervals)
        ans = []
        flag = True
        flag2 = True
        temp = []
        for  i  in range(l):
            if flag :
                if newInterval[0]<intervals[i][0]:
                    temp.append(newInterval[0])
                    flag = False
                elif newInterval[0]<=intervals[i][1] or newInterval[0]==intervals[i][0]:
                    temp.append(intervals[i][0])
                    flag = False
                else:
                    ans.append(intervals[i])
            if not flag and flag2:
                if newInterval[1]<intervals[i][0]:
                    temp.append(newInterval[1])
                    ans.append(temp)
                    flag2  = False
                elif newInterval[1]<=intervals[i][1] or newInterval[1]==intervals[i][0]:
                    temp.append(intervals[i][1])
                    ans.append(temp)
                    flag2 = False
                    continue
                elif i ==l-1 :
                    temp.append(newInterval[1]) 
                    ans.append(temp)
            if not flag2:
                ans.append(intervals[i])
        if not temp:
            ans.append(newInterval)
        return ans
    # 官方的解法 思路基本一致
    def insert_official(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        
        if not placed:
            ans.append([left, right])
        return ans
s = Solution()
print(s.insert([[1,5]],[4,8]))
            
                

        