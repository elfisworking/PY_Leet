from typing import List
class N:
        def __init__(self,value:int,path:[int]):
            self.value = value
            self.path = path

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        RootNode = N(0,[])
        ans = []
        l = len(candidates)
        def deep(rootNode:N,candidates:List[int],t:int,begin:int):
            for i in range(begin,l):
                if rootNode.value + candidates[i] == t:
                    new_path = [i for i in rootNode.path]
                    new_path.append(candidates[i])
                    if new_path not in ans:
                        ans.append(new_path)
                    return
                if  rootNode.value + candidates[i] > t or i+1<l and rootNode.value + candidates[i] + candidates[i+1] > t:
                    continue
                if rootNode.value + sum(candidates[i:]) < target:
                    return 
                new_path = [i for i in rootNode.path]
                new_path.append(candidates[i])
                newNode = N(candidates[i]+rootNode.value,new_path)
                deep(newNode,candidates,t,i+1)
        deep(RootNode,candidates,target,0)

        return ans
    def combinationSum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res
s = Solution()
print(s.combinationSum_2([1,1,1],3))
        