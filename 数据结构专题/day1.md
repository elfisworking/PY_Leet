# day1

## 136. 只出现一次的数字
* https://leetcode-cn.com/problems/single-number/

异或运算

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
```

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(auto i : nums) {
            ans ^= i;
        }
        return ans;
    }
};
```

```java
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for(int n : nums) {
            ans ^= n;
        }
        return ans;

    }
}
```

## 169. 多数元素
* https://leetcode-cn.com/problems/majority-element/

摩尔投票算法

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if not count:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1            
        return candidate
```

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;
        for(int num : nums) {
            if(!count) {
                candidate = num;
            }

            if(candidate == num) {
                count ++;
            }else {
                count --;
            }
        }
    return candidate;
    }
};
```

```java
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;
        for(int num : nums) {
            if(count == 0) {
                candidate = num;
            }

            if(candidate == num) {
                count++;
            }else {
                count--;
            }
        }
        return candidate;
    }
}
```

## 
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        ans = []
        l = len(nums)
        index = 0
        for index in range(l):
            if nums[index] > 0:
                break
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            left, right = index + 1, l - 1
            while left < right:
                value = nums[index] + nums[left] + nums[right]
                if value == 0:
                    ans.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif value > 0:
                    right -= 1
                else:
                    left += 1
        return ans
```