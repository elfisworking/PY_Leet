# 在快速排序中，很重要的一步就是根据pivot进行划分，下面写了几种划分方式，以供参考
# 使用双指针的方式进行排序


nums = [2,3,1,1] # nums是用于排序的数组

def sort(nums:list,target):
    l = len(nums)
    left , right = 0 , l-2
    nums[0],nums[l-1] = nums[l-1],nums[0]
    while True:
        while  nums[left] < nums[l-1]:
            left += 1
        while nums[right] >= nums[l-1]:
            right -= 1
        if left < right:
            nums[left] , nums[right] = nums[right],nums[left]
        else:
            break
    nums[left] ,nums[l-1]= nums[l-1] , nums[left]
    print(nums)

def quick_sort(l,r):
    if l >= r:
        return 
    # 选择left这个位置来临时存放pivot
    left , right = l, r
    tmp = nums[left]
    while left < right:
        while left < right and nums[right] >= tmp: # 等于号用于处理和pivot值相同的元素
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < tmp:
            left += 1
        nums[right] = nums[left]
    nums[left] = tmp
    quick_sort(l,left-1)
    quick_sort(left+1,r)
    
# 这是一种快慢指针的方式来进行的partion
def quick_sort_version2(nums):
    l = len(nums)
    pivot = nums[l-1]
    i = -1
    for j in range(0,l-1):
        if nums[j]<=pivot:
            i += 1
            nums[i] , nums[j] = nums[j] , nums[i]
    nums[i+1] , nums[l-1] = nums[l-1] , nums[i+1]
    print(nums)

# 但是上述的两种的两种做法，对于当切点即pivot为重复元素时，不太友好
# 可以使用下面的方法进行改进 不过这里需要三个三个指针
def quick_sort_version3(nums):
    l = len(nums)
    pivot = nums[l-1]
    # a b c 三个指针
    b = -1
    c = -1
    for a in range(l-1):
        if nums[a] < pivot:
            b += 1
            c += 1
            nums[c] , nums[a] = nums[a],nums[c]
            nums[c] , nums[b] = nums[b],nums[c]
        elif nums[a] == pivot:
            c += 1
            nums[c] , nums[a] = nums[a],nums[c]
    nums[c+1] , nums[l-1] = nums[l-1],nums[c+1]
    print(nums)

def quick_sort_IBM(nums,l,r):
    if l >= r:
        return 
    pivotValue = nums[l]
    left , right = l-1 ,r + 1

    while True:
        # 与官方的差异在注释的这部分  似乎每一都应该--right
        right -= 1
        while nums[right] > pivotValue:
            right -= 1
        left += 1
        while nums[left] < pivotValue:
            left += 1
        if left >= right:
            break
        nums[left] , nums[right] = nums[right] , nums[left]
    pivot = right
    quick_sort_IBM(nums,l,pivot)
    quick_sort_IBM(nums,pivot+1,r)

def quick_sort_leetcode(strs,l , r):
    if l >= r: return
    i, j = l, r
    while i < j:
        while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
        while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
        strs[i], strs[j] = strs[j], strs[i]
    strs[i], strs[l] = strs[l], strs[i]
    quick_sort(l, i - 1)
    quick_sort(i + 1, r)

quick_sort(0,len(nums)-1)
print(nums)