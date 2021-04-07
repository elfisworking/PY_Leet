# 求非降序范围[first, last)内第一个不小于value的值的位置
def lower_bound(array, first, last, value):  #
    while first < last: # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2  # 防溢出
        if array[mid] < value: first = mid + 1 
        else: last = mid
    return first  # last也行，因为[first, last)为空的时候它们重合
# 求非降序范围[first, last)内第一个最后一个等于value的值的位置
def higher_bound(nums,target):
    left , right =  0,len(nums)# 注意
    while left < right:# [left,right)
        mid = (left+right)//2
        if nums[mid] == target:
            left = mid + 1 # 注意
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left-1
# 以下的二分搜索虽然也能够使用，但是存在缺陷，没有上面的好
def binary_search(nums,target):
    # 注意right的边界
    left , right = 0 , len(nums)-1
    # 为什么 while 循环的条件中是 <=，而不是 < ？
    # 答：因为初始化 right 的赋值是 nums.length - 1，
    # 即最后一个元素的索引，而不是 nums.length。
    while left<= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid # 注意
        elif nums[mid] < target:
            left = mid+1 # 注意
        else:
            right = mid -1  # 注意
    return -1
