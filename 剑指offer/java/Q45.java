
//
//
/*
@File : Q45.java
@Time : 2021/07/11 10:01:47
@Author : YuMin Zhang
*/
public class Q45 {
    public String minNumber(int [] nums){
        String [] strs =  new String[nums.length];
        for(int i = 0 ; i < nums.length; i++){
            strs[i] = String.valueOf(nums[i]);
        }
        quickSort(strs, 0, strs.length-1);
        StringBuilder ans = new StringBuilder();
        for(String i : strs){
            ans.append(i);
        }
        return ans.toString();
    }
    public void quickSort(String [] strs,int l , int r){
        if(l >= r){
            return; 
        }
        int left = l , right = r;
        String tmp = strs[l];
        while( left < right){
            while( left < right && (strs[left] + tmp).compareTo(tmp+strs[left]) < 0) left++;
            strs[right] = strs[left];
            while( left < right && (strs[right] + tmp).compareTo(tmp + strs[right]) >= 0) right--;
                strs[left] = strs[right];

        }
        strs[left] = tmp;
        quickSort(strs, l, left-1);
        quickSort(strs, left+1, r);
    }

    public static void main(String[] args) {
        Q45 solution = new Q45();
        System.out.println(solution.minNumber(new int[]{1,2,2,3,1}));
    }
}
