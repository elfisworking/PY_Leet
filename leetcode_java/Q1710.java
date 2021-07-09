package leetcode_java;
// 面试题 17.10. 主要元素
// https://leetcode-cn.com/problems/find-majority-element-lcci/
class Q1710 {
    public int majorityElement(int[] nums) {
        int candidate = -1;
        int cnt = 0;
        for(int i : nums){
            if(cnt == 0){
                cnt = 1;
                candidate = i;
            }else{
                if(candidate == i){
                    cnt++;
                }
                else{
                    cnt--;
                }
            }
        }
        if(cnt == 0) return -1;
        
        int counter = 0;
        for(int i : nums){
            if(i == candidate) counter++;
        }
        return counter > nums.length/2 ? candidate : -1;

    }
}