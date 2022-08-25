# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
# 自顶向下的建堆方式 O(nlog2n)
# 自下向上的建堆方式 O(n)
def 



def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
    print("%d" % arr[i]),
# This code is contributed by Mohit Kumra
## 数组中的第K个最大元素
class Solution:
    def heapify(self, nums, i, heapsize):
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2
        if left < heapsize and nums[left] > nums[largest]:
            largest = left
        if right < heapsize and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, largest, heapsize)
    
    def findKthLargest(self, nums, k: int) -> int:
        heapsize = len(nums)
        for i in range(heapsize // 2 ,  -1, -1):
            self.heapify(nums, i, heapsize)
        
        for i in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            self.heapify(nums, 0, heapsize)
        return nums[0]

s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))