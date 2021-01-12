# 不满足时间复杂度 写的内存占用太多了
def findMedianSortedArrays_1(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        odd = ( m+ n )%2
        #是奇数
        med_index = 0
        if odd == 1:
            med_index = (m+n-1)//2 
        else:
            med_index = (m+n) //2 -1 
        count=0
        index_one=0
        index_two=0
        while index_one<m and index_two<n:
            if(nums1[index_one] <= nums2[index_two]):
                if count == med_index:
                    if odd == 0:
                        next_med = nums1[index_one+1] if (index_one+1)< m and nums1[index_one+1] < nums2[index_two] else nums2[index_two]
                        return (nums1[index_one]+next_med)/2
                    else:
                        return nums1[index_one]
                index_one += 1
                count += 1
            else:
                if count == med_index:
                    if odd == 0:
                        next_med = nums2[index_two+1] if (index_two+1)< n and nums2[index_two+1]<nums1[index_one] else nums1[index_one]
                        return (nums2[index_two]+next_med)/2
                    else:
                        return nums2[index_two]
                index_two += 1
                count += 1
        if  m < n:
            while index_two < n:
                if count == med_index:
                    if odd == 0:
                        return (nums2[index_two]+nums2[index_two+1])/2
                    else:
                        return nums2[index_two]
                index_two += 1
                count += 1
        else:
            while index_one < m:
                if count == med_index:
                    if odd == 0:
                        return (nums1[index_one]+nums1[index_one+1])/2
                    else:
                        return nums1[index_one]
                index_one += 1
                count += 1


def findMedianSortedArrays_2(nums1,nums2):
    def getKthElement(k):
        index1 ,index2 =0,0
        while True:
            if index1 == m:
                return nums2[index2+k-1]
            if index2 == n:
                return nums1[index1+k-1]
            if k == 1:
                return min(nums1[index1],nums2[index2])
            # 正常情况
            newIndex1 = min(index1+k//2 -1,m-1)
            newIndex2 = min(index2+k//2 -1,n-1)
            pivot1,pivot2 = nums1[newIndex1],nums2[newIndex2]
            if pivot1 < pivot2:
                k -= newIndex1-index1+1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2-index2 + 1
                index2 = newIndex2 + 1
    m,n = len(nums1),len(nums2)
    total_length = m + n
    if total_length % 2 == 1:
        return getKthElement((total_length+1)//2)
    else:
        return (getKthElement(total_length//2)+getKthElement(total_length//2 +1))/2

print(findMedianSortedArrays_2([1,2],[3,4]))