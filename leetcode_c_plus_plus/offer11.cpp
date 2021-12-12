// 剑指 Offer 11. 旋转数组的最小数字
// https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer11.cpp
@Time : 2021/11/30 19:47:32
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int minArray(vector<int>& numbers) {
        numbers.push_back();
        int left = 0, right = numbers.size() - 1;
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(numbers[right] < numbers[mid]) left = mid + 1;
            else if (numbers[right] > numbers[mid]) right = mid;
            else right--;
        }
        return numbers[left];

    }
};