# 摩尔投票算法
# 用途：找出大于一半的数

# Boyer-Moore 投票算法的步骤如下：
# 维护一个候选主要元素candidate 和候选主要元素的出现次数 count，初始时 candidate 为任意值，count=0；
# 遍历数组 nums 中的所有元素，遍历到元素 xx 时，进行如下操作：
# 如果 count=0，则将 xx 的值赋给 candidate，否则不更新 candidate 的值；
# 如果 x=candidate，则将 count 加 1，否则将 count 减 1。
# 遍历结束之后，如果数组 nums 中存在主要元素，则 candidate 即为主要元素，否则 candidate 可能为数组中的任意一个元素。
# 由于不一定存在主要元素，因此需要第二次遍历数组，验证 candidate 是否为主要元素。第二次遍历时，统计 candidate 在数组中的出现次数，如果出现次数大于数组长度的一半，
# 则 candidate 是主要元素，返回 candidate，否则数组中不存在主要元素，返回 -1。

def boyer_moore_algrothim(nums: list):
    candidate = -1
    count = 0
    for num in nums:
        if not count:
            candidate = num
        if num == candidate:
            count +=1
        else:
            count -=1
    
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    return candidate if count * 2 > len(nums) else -1
