from typing import List
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     不超时 但是时间消耗高
#     def sumRange(self, i: int, j: int) -> int:
#         temp = 0
#         for a in range(i,j+1):
#             temp += self.nums[a]
#         return temp
# class NumArray:
#      使用这种动态存储答案 超时 不要使用二维数组 使用一维数组 通过[i,j]=[0,j]-[0,i]来求
#     def __init__(self, nums: List[int]):
#         l = len(nums)
#         res = [ [ 0 for _ in range(l)] for _ in range(l)]
#         for i in range(l):
#             res[i][i] = nums[i]
#         for a in range(l):
#             for b in range(a+1,l):
#                 res[a][b] = res[a][b-1]+nums[b]
#         self.nums = res


#     def sumRange(self, i: int, j: int) -> int:
#         return self.nums[i][j]
class NumArray:
    # 这样写存在一个问题 当nums等于空时会出错 需要进行判断 同时需要存储nums 空间复杂度变大
    # 通过注释这样的写法可以避免存储nums里面的信息
    def __init__(self, nums: List[int]):
        l  = len(nums)
        if l == 0:
            return 
        res = [0]*l
        res[0] = nums[0]
        for i in range(1,l):
            res[i] = res[i-1]+nums[i]
        self.res = res
        self.nums = nums
        # res[0] = 0
        # for i in range(l):
        #     res.append(res[-1]+nums[i])
        # self.res= res
            
            
    def sumRange(self, i: int, j: int) -> int:
        return  self.res[j]-self.res[i]+self.nums[i]
        # return  self.res[j+1]-self.res[i]

arr = NumArray([-2, 0, 3, -5, 2, -1])
print(arr.sumRange(2,5))