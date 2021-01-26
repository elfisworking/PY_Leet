class Solution:
    def myPow(self, x: float, n: int) -> float:
        def bin(x,n):
            if n == 1:
                return x
            if n%2 == 0:
                n = n//2
                y = bin(x,n)
                # return bin(x,n)*bin(x,n)这么写超时 因为重复计算了两次
                return y * y
            else:
                n =( n-1)//2      
                y = bin(x,n)
                return x * y *y
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n >0:
            return bin(x,n)
        n = abs(n)
        return 1/bin(x,n)
        # 这个递归方式可以
    def myPow_1(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            # 官方的处理方式非常的好
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
s = Solution()
print(s.myPow(2,9))

        