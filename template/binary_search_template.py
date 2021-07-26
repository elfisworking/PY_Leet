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

# 这个版本的二分查找写错了 不知道为什么原因
def binary_search_error_version(nums:list,target):
    l = len(nums)
    left , right = 0 , l # [left,right}
    while left < right:
        mid = ( left +  right  ) //2 
        if nums[mid] <= target:
            left = mid  # 这里错误了 这里应该修改为mid+1
        else:
            right = mid -1  # 这里应该修改为 mid

def binary_search_right(nums:list,target:int):
    if not nums:
        return None
    left , right = 0 , len(nums)
    while left < right:
        mid =  left + (right - left)//2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left -1 

# 以下为Go代码的二分搜索会出现的乱七八糟的情况
# func FirstGreaterOrEqual(array []int, target int) int {
#     // 初始化区间左端点： -1  ||  0  ||  1  ？
#     l := 0
#     // 初始化区间右端点： len(array) - 1  ||  len(array)  ||  len(array) + 1  ?
#     r := len(array)
#     // 当区间不为空时循环： l + 1 < r  ||  l < r  ||  l <= r  ||  l <= r + 1  ?
#     for l < r {
#         // 计算区间中点： l + (r - l) / 2  ||  l + (r - l + 1) / 2  ?
#         m := l + (r - l) / 2
#         // 将中点对应的元素同target比较： >  ||  >=  ||  <  || <=  ?
#         if array[m] < target {
#             // 继续查找右侧这一半： m - 1  ||  m  ||  m + 1  ?
#             l = m + 1
#         } else {
#             // 继续查找左侧这一半： m - 1  ||  m  ||  m + 1  ?
#             r = m
#         }
#     }
#     // 这里应该是 l - 1  ||  l  ||  l + 1  ?
#     // 这里应该是 r - 1  ||  r  ||  r + 1  ?
#     return l
# }

if __name__ == "__main__":
    nums = [1,2,6,6,6,7]
    print(binary_search_right(nums,7))