// 295. 数据流的中位数
// https://leetcode-cn.com/problems/find-median-from-data-stream/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
#include<queue>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 295.cpp
@Time : 2022/01/03 22:06:16
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Hard
**/
class MedianFinder {
private:
    priority_queue<int, vector<int>, greater<int>> small;
    priority_queue<int, vector<int>, less<int>> big;
public:
    MedianFinder() {

    }
    
    void addNum(int num) {
        if(small.size() == big.size()) {
            if(small.size() != 0 && num < small.top()) big.push(num);
            else {
                small.push(num);
                int s = small.top();
                small.pop();
                big.push(s);
            }
        } else {
            if(big.size() != 0 && num > big.top()) small.push(num);
            else {
                big.push(num);
                int b = big.top();
                big.pop();
                small.push(b);
            }
        }

    }
    
    double findMedian() {
        if(small.size() == big.size()) return (double)(small.top() + big.top()) / 2.0;
        return double(big.top());
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */