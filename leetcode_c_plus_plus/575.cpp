// https://leetcode-cn.com/problems/distribute-candies/
// 575.分糖果
#include<set>
#include<vector>
using namespace std;

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int> myset;
        for(auto i : candyType){
            myset.insert(i);
        }
        int num = candyType.size() / 2;
        int types = myset.size();
        return num > types ? types : num;
    }
};