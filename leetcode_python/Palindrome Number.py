class Solution:
    # method 1 :solve it by converting the integer to string
    def isPalindrome(self, x: int) -> bool:
        return True if (str(x) == str(x)[::-1]) else False
    # method 2: may be face overflow problem if we reverse all number
    def isPalindrome_2(self,x:int)-> bool:
        if x < 0:
            return False
        sum = 0
        temp = x
        while x// 10 != 0:
            y = x%10
            sum = sum*10 + y
            x = x // 10
        sum  = sum * 10 + x
        print(sum)
        if sum == temp:
            return True
        return False
    # method 3 : only reverse half number
    def isPalindrome_3(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10

s = Solution()
print(s.isPalindrome_2(12021))