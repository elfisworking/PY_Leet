// 剑指 Offer 43. 1～n 整数中 1 出现的次数
// https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
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
@File : offer43.cpp
@Time : 2021/12/27 22:24:16
@Author : YuMin Zhang
@State : Depedent 
@Thinking : 想象以下开锁， 固定一位其他位有多少种可能
@Tag : Hard
**/
class Solution {
public:
    int countDigitOne(int n) {
        long long  digit = 1, res = 0;
        long long high = n / 10, curr = n % 10, low = 0;
        while(high != 0 || curr != 0) {
            if(curr == 0) res += high * digit;
            else if(curr == 1) res += high * digit + low + 1;
            else {
                res += (high + 1) * digit;
            }
            low += curr * digit;
            curr = high % 10;
            high /= 10;
            digit *= 10;
        }
        return int(res);
    }
};

class Solution {
public:
    int countDigitOne(int n) {
        // mulk 表示 10^k
        // 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        // 但为了让代码看起来更加直观，这里保留了 k
        long long mulk = 1;
        int ans = 0;
        for (int k = 0; n >= mulk; ++k) {
            ans += (n / (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0LL), mulk);
            mulk *= 10;
        }
        return ans;
    }
};
