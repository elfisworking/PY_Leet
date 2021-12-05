// 剑指 Offer 47. 礼物的最大价值
// https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer47.cpp
@Time : 2021/12/05 21:20:56
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
int maxValue(vector<vector<int>>& grid)
{
	for (int i = 0,j=1; j < grid[0].size(); j++)	//处理第一行
	{
		grid[i][j] += grid[i][j - 1];
	}
	for (int i = 1,j=0; i < grid.size(); i++)		//处理第一列
	{
		grid[i][j] += grid[i-1][j];
	}
	for (int i = 1; i < grid.size(); i++)
	{
		for (int j = 1; j < grid[0].size(); j++)
		{
			if (grid[i - 1][j] >= grid[i][j - 1])	grid[i][j] += grid[i - 1][j];
			else grid[i][j] += grid[i][j - 1];
		}
	}
	return grid[grid.size()-1][grid[0].size()-1];
}
};