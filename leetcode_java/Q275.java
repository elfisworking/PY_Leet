// 275. H 指数 II
// https://leetcode-cn.com/problems/h-index-ii/
/*
@File : Q275.java
@Time : 2021/07/12 09:48:15
@Author : YuMin Zhang
*/
public class Q275 {
    public int hIndexSolutionOne(int[] citations) {
        // 时间复杂度O(n)
        int length = citations.length;
        int h = 1;
        for(int i = length-1;i>=0;i--){
            if(citations[i] >= h){
                h++;
            }else{
                break;
            }
        }
        return h-1;
    }
    // binary search
    public int hIndex(int[] citations) {
        int left = 0 , right = citations.length;
        while(left<right){
            int mid = left + (right-left)/2;
            if(this.check(citations,mid)){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return citations.length-left;

    }
    public boolean check(int [] citations,int mid){
        if(citations.length-mid<=citations[mid]){
            return true;
        }
        return false;
    }

    
}
