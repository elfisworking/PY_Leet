package java;

class Solution {
    //==================这个方法超时=====================\\
    // public boolean isScramble(String s1, String s2) {
    //     if (s1.equals(s2)) return true;
    //     if (!check(s1, s2)) return false;
    //     int n = s1.length();
    //     for (int i = 1; i < n; i++) {
    //         // s1 的 [0,i) 和 [i,n)
    //         String a = s1.substring(0, i), b = s1.substring(i);
    //         // s2 的 [0,i) 和 [i,n)
    //         String c = s2.substring(0, i), d = s2.substring(i);
    //         if (isScramble(a, c) && isScramble(b, d)) return true;
    //         // s2 的 [0,n-i) 和 [n-i,n)
    //         String e = s2.substring(0, n - i), f = s2.substring(n - i);
    //         if (isScramble(a, f) && isScramble(b, e)) return true;
    //     }
    //     return false;
    // }
    // // 检查 s1 和 s2 词频是否相同
    // boolean check(String s1, String s2) {
    //     if (s1.length() != s2.length()) return false;
    //     int n = s1.length();
    //     int[] cnt1 = new int[26], cnt2 = new int[26];
    //     char[] cs1 = s1.toCharArray(), cs2 = s2.toCharArray();
    //     for (int i = 0; i < n; i++) {
    //         cnt1[cs1[i] - 'a']++;
    //         cnt2[cs2[i] - 'a']++;
    //     }
    //     for (int i = 0; i < 26; i++) {
    //         if (cnt1[i] != cnt2[i]) return false;
    //     }
    //     return true;
    // }
    //==================
    public int strStr(String haystack, String needle) {
        int left = 0;
        int right = 0;
        int res = -1;
        char [] a = haystack.toCharArray();
        char [] b = needle.toCharArray();
        int end = a.length-b.length;
        while(left<end){
            if(a[left]==(b[0])){
                right = left;
                boolean flag  = true;
                for(int i = 0;i<b.length;i++){
                    if(a[right]==b[i]){
                        right++;
                    }else{
                        left = right;
                        flag = false;
                        break;
                    }
                if(flag){
                    return left;
                }
                }
            }else{
            left++;
            }
        }
        return  res;

    }
    public static void main(String[] args) {
        So
    }
}
