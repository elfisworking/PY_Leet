# 1723. 完成所有工作的最短时间
# https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/
from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(limit):
            arr = sorted(jobs)
            
            groups = [0]*k
            # 分成K 组，看看在这个limit 下 能不能安排完工作
            if backtrace(arr,groups,limit):
                return True
            else:
                return False

    
        def backtrace(arr,groups,limit):
            # 尝试每一种可能性
            if not arr: return True # 分完，说明方案可行
            v = arr.pop()
            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr,groups,limit):
                        return True
                    groups[i] -= v

                    if groups[i] == 0:
                        break
            
            arr.append(v)
            return False

            l , r = max(jobs),sum(jobs)

            while l < r:
                mid = (l+r)//2

                if check(mid):
                    r = mid
                else:
                    l = mid + 1
            return l
        
