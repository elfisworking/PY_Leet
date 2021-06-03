from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i  in range(n):
                nums1[i] = nums2[i]
        else:
            for a in nums2:
                for b in range(m-1,-1,-1):
                    if nums1[b] > a:
                        nums1[b+1] = nums1[b]
                        nums1[b] = a
                    else:
                        nums1[b+1] = a
                        break
                m = m + 1

    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)-1
        n = n-1
        m = m-1
        while n>=0:
            while m>=0 and nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m = m - 1
                i = i-1
            nums1[i] = nums2[n]
            n = n - 1
            i = i -1
s = Solution()
print(s.merge_2([1,2,3,0,0,0],3,[2,5,6],3))