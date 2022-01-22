from typing import List
import collections
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A,K)-self.atMostK(A,K-1)
    def atMostK(self, A, K):
        N = len(A)
        left, right = 0, 0
        counter = collections.Counter()
        distinct = 0
        res = 0
        while right < N:
            if counter[A[right]] == 0:
                distinct += 1
            counter[A[right]] += 1
            while distinct > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    distinct -= 1
                left += 1
            res += right - left + 1
            right += 1
        return res
s = Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3],2))

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left1, left2, right = 0, 0, 0
        counter1, counter2 = defaultdict(int), defaultdict(int)
        ans = 0
        while right < len(nums):
            counter1[nums[right]] += 1
            counter2[nums[right]] += 1
            while len(counter1.keys()) > k:
                if counter1[nums[left1]] > 0:
                    counter1[nums[left1]] -= 1
                if counter1[nums[left1]] == 0:
                    del counter1[nums[left1]]
                left1 += 1
            while len(counter2.keys()) > k - 1:
                if counter2[nums[left2]] > 0:
                    counter2[nums[left2]] -= 1
                if counter2[nums[left2]] == 0:
                    del counter2[nums[left2]]
                left2 += 1
            right += 1
            ans += left2 - left1
        return ans