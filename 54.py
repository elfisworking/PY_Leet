from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        begin = 0
        left = 0
        height = len(matrix)-1
        width = len(matrix[0])-1
        ans = []
        # 使用转圈圈的思路  还有一种判断循环终止的条件：记录总数，每处理一个数 总数减一
        # 当总数==0时说明所有的数都已经放进去了 循环终止
        while begin<=height and left<=width:
            # 处理第一行
            for i in range(begin,width+1):
                ans.append(matrix[begin][i])
            # 处理右壁
            if begin+1<height:
                for i in range(begin+1,height):
                    ans.append(matrix[i][width])
            if begin<height:
                # 处理最后一行
                for i in range(width,begin-1,-1):
                    ans.append(matrix[height][i])
            # 处理左壁
            if begin+1<height and left<width:
                for i in range(height-1,begin,-1):
                    ans.append(matrix[i][left])
        
            begin += 1
            height -= 1
            left +=1
            width -=1
        return ans
s = Solution()
print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
