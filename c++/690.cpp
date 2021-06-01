using namespace std;
#include <vector>
#include <unordered_map>
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};

class Solution {
public:
    unordered_map<int,vector<int>> m;
    unordered_map<int,int> imp;
    int getImportance(vector<Employee*> employees, int id) {
        for(auto e : employees){
            m[e->id] = e->subordinates;
            imp[e->id] = e->importance;
        }
        return getValue(id);
        
    }
    int getValue(int id){
        int res =  imp[id];
        for(auto id : m[id]){
            res += getValue(id);
        }
        return res;
    }
};