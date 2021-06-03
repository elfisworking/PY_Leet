# problem name : longest substring without repeating characters
#内存消耗过大因为 因为用两个list保存了所有的信息 可以进行删减 减少内存消耗
def lengthOfLongestSubstring_1(s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        maxLength = 1
        length = []
        start = []
        for index , value in enumerate(s):
            if index  == 0:
                length.append(1)
                start.append(0)
            else:
                sindex = start[index -1 ]
                sub  = s[sindex:index]
                exist = sub.find(value)
                if exist != -1:
                    length.append(index-(sindex+exist))
                    start.append(sindex+exist+1)
                else:
                    length.append(length[index-1]+1)
                    start.append(start[index-1])
        maxLength = max(length)
        return maxLength
## 采用滑动窗口的方法
def lengthOfLongestSubstring_2(s):
        """
        :type s: str
        :rtype: int
        """
        hashSet = set()
        length = len(s)
        rindex = -1
        ans = 0
        for i in range(length):
            if i!= 0:
                hashSet.remove(s[i-1])
            while rindex +1 <length and s[rindex + 1] not in hashSet:
                hashSet.add(s[rindex+1])
                rindex += 1
            ans = max(ans,rindex-i+1)
        return ans
s="dvdf"
print(lengthOfLongestSubstring_2(s))

            