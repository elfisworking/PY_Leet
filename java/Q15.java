package java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q15{
    public List<List<Integer>> threeSum(int [] nums){
        List<List<Integer>> res = new ArrayList<>();
        if(nums.length<2){
            return res;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] > 0)
                break;
            if(i > 0 && nums[i-1]==nums[i] )
                continue;
            int left = i+1;
            int right = nums.length -1;
            while(left<right){
                int val = nums[i]+nums[left]+nums[right];
                if(val == 0){
                    List<Integer> ans = new ArrayList<>();
                    ans.add(nums[i]);
                    ans.add(nums[left]);
                    ans.add(nums[right]);
                    res.add(ans);
                    while(left < right && nums[left]==nums[left+1]){
                        left++;
                    }
                    while(left < right && nums[right-1]==nums[right]){
                        right--;
                    }
                    left++;
                    right --;
                }else if(val > 0){
                    right--;
                }else{
                    left++;
                }
            }   
        }
        return res;
    }
    public static void main(String[] args) {
       Q15 s = new Q15();
       System.out.println(s.threeSum(new int[]{1,-1,0}));
    }
}