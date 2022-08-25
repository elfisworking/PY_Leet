## 树的索引从0开始
## 数组的索引也是从0开始
# 建树 时间复杂度O(n)
# s是原始的数组
# d是线段树
# p 是根的编号
# 一般设 d = 4倍的s长度
'''
数组不变，区间查询：前缀和、树状数组、线段树；
数组单点修改，区间查询：树状数组、线段树；
数组区间修改，单点查询：差分、线段树；
数组区间修改，区间查询：线段树。
'''
# https://leetcode.cn/problems/my-calendar-i/solution/by-lfool-xvpv/

from operator import le
from turtle import left, right, up, update


d = []
s = []
def build(l :int, r :int, s : list, d:list, p: int):
    if l == r:
        d[p] = s[l]
        return 
    mid = l  + ((r - l) >> 2)
    # 左节点  
    build(l , mid, s, d, 2 * p + 1)
    build(mid + 1, r, s, d, 2 * p + 2)
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
def update_lazy(l, r, c, s, t, p):
    if l <= s and t <= r:
        d[p] += (t - s + 1) * c
        b[p] += c
        return 
    mid = s + ((t - s) >> 2)
    if b[p] and s < t: # s == t不需要向下传播了
        d[2 * p + 1] += (mid - s + 1) * b[p]
        b[2 * p + 1] +=  b[p]
        d[2 * p + 2] += (t - mid) * b[p]
        b[2 * p + 2] += b[p]
        b[p] = 0
    if l <= mid:
        update_lazy(l, r, c, s, mid, 2 * p + 1)
    if r > mid:
        update_lazy(l, r, c, mid + 1, t, 2 * p + 2)
    d[p] = d[2 * p + 1] + d[2 * p + 2]

    
# 带有懒惰标记的求和
def getSum_lazy(l, r, s, t, p):
    if l <= s and t <= r:
        return d[p]
    mid = s + ((t - s) >> 2)
    if b[p] and s < t: # 可能由问题 
        d[2 * p + 1] += (mid - s + 1) * b[p]
        d[2 * p + 2] += (t - mid) * b[p]
        b[2 * p + 1] += b[p]
        b[2 * p + 2] += b[p]
    sum = 0
    if l <= mid:
        sum += getSum_lazy(l, r, s, mid, 2 * p + 1)
    if r > mid:
        sum += getSum_lazy(l, r, mid + 1, t, 2 * p + 2)
    return sum

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0
class SegmentTree:
    def query(self, node, start, end, left, right):
        if start <= left and right <= end:
            return node.val
        mid = left + (right - left) // 2
        self.pushDown(node, mid - left + 1, right - mid)
        ans = 0
        if start <= mid:
            ans += self.query(node.left, start, end, left, mid)
        if end > mid:
            ans += self.query(node.right, start, end, mid + 1, right)
        return ans
    def update(self, node, start, end, left, right, val):
        if start <= left and right <= end:
            node.val += (right - left + 1) * val
            node.lazy += val
            return
        mid = left + (right - left) // 2
        self.pushDown(node, mid - left + 1, right - mid)
        if start <= mid:
            self.update(node.left, start, end, left, mid, val)
        if end > mid:
            self.update(node.right, start, end, mid + 1, right, val)
        self.pushUp(node)
    
    def pushDown(self, node, leftNum, rightNum):
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()
        node.left.val += leftNum * node.lazy
        node.right.val += rightNum * node.lazy
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0

    def pushUp(self, node):
        node.val = node.right.val + node.left.val
        
""""
/**
 * @Description: 线段树（动态开点）
 * @Author: LFool
 * @Date 2022/6/7 09:15
 **/
public class SegmentTreeDynamic {
    class Node {
        Node left, right;
        int val, add;
    }
    private int N = (int) 1e9;
    private Node root = new Node();
    public void update(Node node, int start, int end, int l, int r, int val) {
        if (l <= start && end <= r) {
            node.val += (end - start + 1) * val;
            node.add += val;
            return ;
        }
        int mid = (start + end) >> 1;
        pushDown(node, mid - start + 1, end - mid);
        if (l <= mid) update(node.left, start, mid, l, r, val);
        if (r > mid) update(node.right, mid + 1, end, l, r, val);
        pushUp(node);
    }
    public int query(Node node, int start, int end, int l, int r) {
        if (l <= start && end <= r) return node.val;
        int mid = (start + end) >> 1, ans = 0;
        pushDown(node, mid - start + 1, end - mid);
        if (l <= mid) ans += query(node.left, start, mid, l, r);
        if (r > mid) ans += query(node.right, mid + 1, end, l, r);
        return ans;
    }
    private void pushUp(Node node) {
        node.val = node.left.val + node.right.val;
    }
    private void pushDown(Node node, int leftNum, int rightNum) {
        if (node.left == null) node.left = new Node();
        if (node.right == null) node.right = new Node();
        if (node.add == 0) return ;
        node.left.val += node.add * leftNum;
        node.right.val += node.add * rightNum;
        // 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add += node.add;
        node.right.add += node.add;
        node.add = 0;
    }
}

"""