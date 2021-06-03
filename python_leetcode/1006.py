class Solution:
    def clumsy(self, N: int) -> int:
        val = [N]
        N -= 1
        index = 0
        while N > 0:
            if index%4 == 0:
                num = val.pop()
                val.append(num*N)
            elif index%4 == 1:
                num = val.pop()
                val.append(int(num/N))
            elif index%4 == 2:
                val.append(N)
            else:
                val.append(-N)
            index += 1
            N -= 1
        return sum(val)
s = Solution()
print(s.clumsy(10))