from typing import List
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.l = l = len(nums)
#         nums.sort()
#         self.nums = nums
#         self.k = k
#     def add(self, val: int) -> int:
#         index = self.l-self.k
#         if index >= 0:
#             if self.nums[index] >= val:
#                 return self.nums[index]
#             if self.k == 1:
#                 if self.nums[index] < val:
#                     self.nums[index]=val
#                     return self.nums[index]
#                 else:
#                     return self.nums[index]
#             if self.k>1 and self.nums[index] < val <= self.nums[index+1]:
#                 self.nums[index] = val
#                 return val
#             for i in range(index+1,self.l):
#                 if self.nums[i] < val :
#                     self.nums[i-1]= self.nums[i]
#                     if i == self.k-1:
#                         self.nums[i] = val
#                 else:
#                     self.nums[i-1] = val
#             return self.nums[index]
#         else:
#             self.l += 1
#             self.nums.append(val)
#             self.nums.sort()
#             return self.nums[0]
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        while len(self.pool) > k:
            heapq.heappop(self.pool)
    #使用小根堆 进行解决
    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
kthLargest =KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3);   #return 4
kthLargest.add(5);   # return 5
kthLargest.add(10);  # return 5
kthLargest.add(9);   # return 8
kthLargest.add(4);   # return 8
