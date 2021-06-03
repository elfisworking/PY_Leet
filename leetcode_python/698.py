# 698. 划分为k个相等的子集
# https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            print('尝试放置数字{}, 剩余数组={}'.format(v, nums))
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    print('尝试放在位置{}, groups变成={} 向下递归'.format(i,groups))
                    if search(groups): return True
                    print('位置{}尝试失败, groups退回成{}'.format(i, groups))
                    groups[i] -= v
                if not group: break # 进行剪枝 避免重复搜索 
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        # 减少搜索的情况
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        # 避免[0,127] 127这个例子的情况
        if k==0 or not any(nums): return True
        return search([0] * k)
s = Solution()
print(s.canPartitionKSubsets([4,3,2,3,5,2,1],4))