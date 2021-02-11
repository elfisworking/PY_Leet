class Solution:
    # 创建两个list 分别为l1和l2。两者的长度都为s1的长度 按照字母循序排序
    # 比较两者 如果两者相等就返回True 否咋False 。在比较的过程中不断的移动
    # l2，从而能够遍历这个s2字符串
    def checkInclusion_1(self, s1: str, s2: str) -> bool:
        l1=[ i for i in s1]
        l1.sort()
        length2= len(s2)
        length1 = len(s1)
        if length1 > length2:
            return False
        l2 =[s2[i] for i in range(length1)]
        left ,right =0, length1-1
        while right<length2:
            l2.sort()
            if l2==l1:
                return True 
            if right+1 < length2:
                l2.remove(s2[left])
                l2.append(s2[right+1])
            right +=1
            left += 1
        return False
    # 使用了hash表  因为只有26个字母 所以直接创建一个大小为26的list即可
    # 然后统计list1 和 list2是否相等即可
    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        l1 , l2 = len(s1),len(s2)
        if l1>l2:
            return False
        cnt1 , cnt2= [0]*26,[0]*26
        bg = ord('a')
        for i in range(l1):
            cnt1[ord(s1[i])-bg] += 1
            cnt2[ord(s2[i])-bg] += 1
        if cnt1 == cnt2:
            return True
        for i in range(l1,l2):
            cnt2[ord(s2[i])-bg] += 1
            cnt2[ord(s2[i-l1])-bg] -= 1
            if cnt2==cnt1:
                return True
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 ,l2 = len(s1),len(s2)
        if l1 > l2:
            return False
        cnt = [0]*26
        bg = ord("a")
        for i in range(l1):
            cnt[ord(s1[i])-bg] -= 1
            cnt[ord(s2[i])-bg] += 1
        diff = 0
        for c in cnt:
            if c != 0:
                diff += 1
        for i in range(l1,l2):
            x = ord(s2[i]) - bg 
            y = ord(s1[i-l1]) - bg
            if x==y:
                continue
            if cnt[x] == 0:
                diff += 1
            cnt[x] += 1
            if cnt[x] == 0:
                diff -= 1
            if cnt[y] == 0:
                diff += 1
            cnt[y] -= 1
            if cnt[y] == 0:
                diff -= 1
            if diff == 0:
                return True
        return False


s  = Solution()
print(s.checkInclusion("ab","eidbaoo"))
