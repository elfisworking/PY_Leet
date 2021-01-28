from typing import List
# 仍然是使用54题的转圈圈思路 先构造出矩阵的结构 然后一次填充数据就可以了
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for a in range(n)]
        begin = 0
        left = 0
        height = n-1
        width =  n-1
        num = 1
        # 使用转圈圈的思路  还有一种判断循环终止的条件：记录总数，每处理一个数 总数减一
        # 当总数==0时说明所有的数都已经放进去了 循环终止
        while begin<=height and left<=width:
            # 处理第一行
            for i in range(begin,width+1):
                matrix[begin][i] = num
                num += 1
                #ans.append(matrix[begin][i])
            # 处理右壁
            if begin+1<height:
                for i in range(begin+1,height):
                    matrix[i][width] = num
                    num +=1
                    # ans.append(matrix[i][width])
            if begin<height:
                # 处理最后一行
                for i in range(width,begin-1,-1):
                    matrix[height][i] = num
                    num +=1
                    #ans.append(matrix[height][i])
            # 处理左壁
            if begin+1<height and left<width:
                for i in range(height-1,begin,-1):
                    matrix[i][left] = num
                    num += 1
                    #ans.append(matrix[i][left])
        
            begin += 1
            height -= 1
            left +=1
            width -=1
        return matrix
    # 官方的解法 但是思路基本一致 只是实现的方式不一样 可以看一下
    def generateMatrix_offical(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat

s =Solution()
print(s.generateMatrix(4))