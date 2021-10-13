# 快速幂
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
# 分治算法
# Non-recursion version

def quick_pow_non_recursion(x: float, n: int) -> float:
    if x == 0.0: return 0.0
    res = 1
    if n < 0:
        x , n = 1 / x, -n
    while n:
        if n & 1: # n & 1 eqaul n%2 == 1
            res *= x
        x *= x
        n >>= 1 # 相当于 n//2
    return res
# x >=0 n >=0 
def quick_pow_recursion(x: float, n: int) -> float:
    if x == 0.0: return 0.0
    if n == 0:
        return 1
    if n == 1:
        return x
    if n & 1:
        return x * quick_pow_recursion(x, n//2)**2
    else:
        return quick_pow_recursion(x, n//2)**2

# 快速乘 改 快速加
def quickAdd(y: int, z: int, x: int) -> bool:
    # x 和 y 是负数，z 是正数
    # 需要判断 z * y >= x 是否成立
    result, add = 0, y
    while z > 0:
        if (z & 1) == 1:
            # 需要保证 result + add >= x
            if result < x - add:
                return False
            result += add
        if z != 1:
            # 需要保证 add + add >= x
            if add < x - add:
                return False
            add += add
        # 不能使用除法
        z >>= 1
    return True