package leetcode_java;
// 45. 跳跃游戏 II
// https://leetcode-cn.com/problems/jump-game-ii/
class Q45 {
    public int jump(int[] nums) {
        int maxLocation = 0;
        int end = 0;
        int step = 0;
        for(int i=0;i<nums.length-1;i++){
            maxLocation = Math.max(maxLocation,i+nums[i]);
            if(i == end){
                end = maxLocation;
                step ++;
            }
        }
        return step;
    }
}