from typing import List
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # relay_set = {}
        # l = len(grid)
        # l1 = len(grid[0])
        # for x in range(0,l):
        #     for y in range(1,l1-1):
        #         if grid[x][y] == 1:
        #             #向4个方向探索
        #             # 向左探索
        #             relay = []
        #             z = y
        #             while z>0 and grid[x][z-1]==1:
        #                 z -= 1
        #             if z == 0:
        #                 relay.append(l1*x)
        #             z = y
        #             while z<l1-1 and grid[x][z+1] == 1:
        #                 z += 1
        #             if z == l1-1:
        #                 relay.append(l1*z+y)
        #             # z = x
        #             # while z > 0  and grid[z-1][y]==1:
        #             #     z -= 1
        #             # if z == 0:
        #             #     relay.append(l1*x)
        #             # z = x
        #             # while z<l-1 and grid[z+1][y] == 1:
        #             #     z +=1
        #             # if z == l -1 :
        #             #     relay.append(l1*x+z)
        #             relay_set[l1*x+y] = relay
        # ans = []
        # for value in hits:
        #     index = l1*value[0]+value[1]
        #     delete = []
        #     for key,value in relay_set.items():
        #         if index in value:
        #             value.remove(index)
        #         if len(value) == 0:
        #             delete.append(key)
        #     for v in delete:
        #         del relay_set[v]        
        #     ans.append(len(delete)) 
        # return ans
s = Solution()
print(s.hitBricks([[1,0,0,0],[1,1,0,0]],[[1,1],[1,0]]))
                
                  
 