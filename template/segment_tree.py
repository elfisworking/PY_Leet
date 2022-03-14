## 树的索引从0开始
## 数组的索引也是从0开始
# 建树 时间复杂度O(n)
# s是原始的数组
# d是线段树
'''
数组不变，区间查询：前缀和、树状数组、线段树；
数组单点修改，区间查询：树状数组、线段树；
数组区间修改，单点查询：差分、线段树；
数组区间修改，区间查询：线段树。
'''
from logging import makeLogRecord


d = []
s = []
def build(l :int, r :int, s : list, d:list, p: int):
    if l == r:
        d[p] = s[l]
        return 
    mid = l  + ((r - l) >> 2)
    # 左节点  
    build(l , mid, s, d, 2 * p + 1)
    build(mid + 1, s, d, 2 * p + 2)
    d[p] = d[2 * p + 1] + d[2 * p + 2]

def getSum(l:int, r:int, s:int, t:int, p:int) -> int:
    # [l, r]是要查询的区间， [s, t]是当前p节点所包含的区间
    # 递归实现
    if l <= s and t <= r:
        return d[p]
    mid = s + (t - s) >> 2
    sum = 0
    if l <= mid:
        sum += getSum(l, r, s, mid, 2 * p + 1)
    if r > mid:
        sum += getSum(l, r, mid + 1, t, 2 * p + 2)
    return sum

# 线段树的区间修改与懒惰标记
# [l, r] 为修改区间, c 为被修改的元素的变化量, [s, t] 为当前节点包含的区间, p
# b 是一个懒惰标记数组
b = []
def update(l, r, c, s, t, p):
    if l <= s and t <= r:
        d[p] += (t - s + 1) * c
        b[p] = c
        return 
    mid = s + ((t - s) >> 2)
    if b[p] and s != t:
        d[2 * p + 1] += (mid - s + 1) * b[p]
        b[2 * p + 1] +=  b[p]
        d[2 * p + 2] += (t - mid) * b[p]
        b[2 * p + 2] += b[p]
        b[p] = 0
    if l <= mid:
        update(l, r, c, s, mid, 2 * p + 1)
    if r > mid:
        update(l, r, c, mid + 1, t, 2 * p + 2)
    d[p] = d[2 * p + 1] * d[2 * p + 2]

    
# 带有懒惰标记的求和
def getSum(l, r, s, t, p):
    if l <= s and t <= r:
        return d[p]
    mid = s + ((t - s) >> 2)
    if b[p]:
        d[2 * p + 1] += (mid - s + 1) * b[p]
        d[2 * p + 2] += (t - mid) * b[p]
        b[2 * p + 1] += b[p]
        b[2 * p + 2] += b[p]
    sum = 0
    if l <= mid:
        sum += getSum(l, r, s, mid, 2 * p + 1)
    if r > mid:
        sum += getSum(l, r, mid + 1, t, 2 * p + 2)
    return sum