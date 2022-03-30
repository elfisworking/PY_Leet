// 面试题 05.03. 翻转数位
// https://leetcode-cn.com/problems/reverse-bits-lcci/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
#include<bitset>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 05.05.cpp
@Time : 2022/03/26 15:08:31
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int reverseBits(int num) {
        bitset<32> bits(num);//记录 num 的二进制 01 串
        int ans = 1 , zero = 0;
        int n1 = 0, n2 = 0;
        int i=0;
        while( i <= 32){
            n1 = n2 ,n2 = 0, zero = 0;
            while(i<=32 && bits[i]==0){
                ++zero;//统计连续的 0 的个数
                ++i;
            }
            while(i<=32 && bits[i]==1){
                ++n2;//统计连续的 1 的个数
                ++i;
            }
            ans = max(ans,n2+1);           
            if(zero==1){ //如果前后的连续为 1 的串中间之隔了一个0
                ans = max(ans,n1+n2+1); //看连接之后是否达到最长
            }
        }
        return min(32,ans); //有可能全为 1 ，此时不用变位已达到最长
    }
};