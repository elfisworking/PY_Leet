package 剑指offer.java;

import java.util.Arrays;

// 274. H 指数
// https://leetcode-cn.com/problems/h-index/
/*
@File : Q274.java
@Time : 2021/07/11 09:47:51
@Author : YuMin Zhang
*/
public class Q274 {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int left = 0;
        int right = citations.length;
        int mid ;
        while(left < right){
            mid = left + (right-left)/2;
            if(this.check(citations,mid)){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return citations.length - left;

    }
    public boolean check(int [] citations , int mid){
        int h = citations.length - mid;
        if(h<=citations[mid]){
            return true;
        }
        return false;
    }
}
