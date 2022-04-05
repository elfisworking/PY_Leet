// 剑指 Offer II 001. 整数除法
// https://leetcode-cn.com/problems/xoh6Oh/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : offerII001.cpp
@Time : 2022/04/01 21:58:08
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int divide(long long a, long long b) {
        bool flag = false;
        long long tmp = a * b;
        if(tmp < 0.0 ) flag = true;
        a = abs(a);
        b = abs(b);
        if(b > a) return 0;
        long long ans = 1;
        long long left = 1; 
        long long right = a + 1;
        while(left < right) {
            long long mid = left + (right - left) /2;
            if(mid * b >= a) right = mid;
            else left = mid + 1;
        }
        ans = left;
        // cout << flag << endl;
        if(ans * b > a)  --ans;
        if(flag) ans = -ans;
        if(ans >= 2147483647) return 2147483647;
        return ans;
    }
};

class Solution {
    int INF = Integer.MAX_VALUE;
    public int divide(int _a, int _b) {
        long a = _a, b = _b;
        boolean flag = false;
        if ((a < 0 && b > 0) || (a > 0 && b < 0)) flag = true;
        if (a < 0) a = -a;
        if (b < 0) b = -b;
        long l = 0, r = a;
        while (l < r) {
            long mid = l + r + 1 >> 1;
            if (mul(mid, b) <= a) l = mid;
            else r = mid - 1;
        }
        r = flag ? -r : r;
        if (r > INF || r < -INF - 1) return INF;
        return (int)r;
    }
    long mul(long a, long k) {
        long ans = 0;
        while (k > 0) {
            if ((k & 1) == 1) ans += a;
            k >>= 1;
            a += a;
        }
        return ans;
    }
}
