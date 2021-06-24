# 剑指 Offer 04. 二维数组中的查找
# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 注意 
        if not matrix or not matrix[0]:
            return False
        colLengh = len(matrix[0])
        for row in matrix:
            if row[-1]<target:
                continue
            if row[0] > target:
                break
            for i in range(colLengh):
                if row[i] == target:
                    return True
        return False