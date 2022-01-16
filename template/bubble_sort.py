'''
冒泡排序
思想：进行n次循环，每次把最大值移动到list右边
'''
def bubble_sort(nums:list):
    l = len(nums)
    for i in range(l):
        for j in range(1,l - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    print(nums)

bubble_sort([1, 5, 3])
bubble_sort([1])
bubble_sort([1,3,4,5])