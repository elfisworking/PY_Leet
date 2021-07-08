package 剑指offer.java;

public class Q42 {
        public int maxSubArray(int[] nums) {
            int tmp = nums[0];
            int max = nums[0];
            for(int i=1; i < nums.length; i++){
                tmp = Math.max(nums[i],tmp+nums[i]);
                max = Math.max(tmp,max);
            }
            return max;
    
        }
}
