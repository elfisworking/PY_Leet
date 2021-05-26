# 在快速排序中，很重要的一步就是根据pivot进行划分，下面写了几种划分方式，以供参考
# 使用双指针的方式进行排序
def sort(nums:list,target):
    l = len(nums)
    left , right = 0 , l-2
    nums[0],nums[l-1] = nums[l-1],nums[0]
    print(nums)
    i = 1
    while True:
        while  nums[left] < target:
            left += 1
        while nums[right] >= target:
            right -= 1
        if left < right:
            nums[left] , nums[right] = nums[right],nums[left]
            print(i,nums,"left:",left,"right:",right)
            i += 1
        else:
            break
    nums[left] ,nums[l-1]= nums[l-1] , nums[left]
    print(nums)
# 这是一种快慢指针的方式来进行的partion
def quick_sort(nums):
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
def quick_sort_version2(nums):
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


nums = [3,6,3,2,4,3]
# print(0,nums)
# # sort(nums,3)
# quick_sort_version2(nums)
print(nums+[0])