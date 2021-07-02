from typing import List
class N:
        def __init__(self,value:int,path:[int]):
            self.value = value
            self.path = path

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        RootNode = N(0,[])
        ans = []
        def deep(rootNode:N,candidates:List[int],t:int,begin:int):
            for i in range(begin,len(candidates)):
                
                if rootNode.value + candidates[i] == t:
                    new_path = [i for i in rootNode.path]
                    new_path.append(candidates[i])
                    ans.append(new_path)
                    return
                if rootNode.value + candidates[i] > t or rootNode.value + candidates[i] + candidates[0] > target:
                    continue
                new_path = [i for i in rootNode.path]
                new_path.append(candidates[i])
                newNode = N(candidates[i]+rootNode.value,new_path)
                deep(newNode,candidates,t,i)
        deep(RootNode,candidates,target,0)

        return ans
s = Solution()
        