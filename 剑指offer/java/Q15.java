package 剑指offer.java;

public class Q15 {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans=0;
        while(n!=0){
            ans += n & 1;
            // >>>  is unsigned right shift operator
            n = (n >>> 1);
        }
        return ans;
    }
}