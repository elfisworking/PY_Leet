package leetcode_java;
// 26. 删除有序数组中的重复项
// https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
class Q26 {
    // 相当于一个快慢指针，慢指针指向返回的数组长度，快指针用于判断重复元素
    public int removeDuplicates(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        int res = 1;
        for(int i = 1 ; i<nums.length;i++){
            if(nums[i]!= nums[i-1]){
                nums[res] = nums[i];
                res++;
            }
        }
        return res;
    }
}