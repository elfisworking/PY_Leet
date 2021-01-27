from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        temp=intervals[0]
        ans = []
        for pair in intervals:
            if temp[0]<=pair[0]<=temp[1]:
                if temp[1]<pair[1]:
                    temp[1]=pair[1]
            else:
                ans.append(temp)
                temp=pair
        ans.append(temp)
        return ans
s = Solution()
print(s.merge([[1,4],[2,3]]))
