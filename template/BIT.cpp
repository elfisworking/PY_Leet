// 构建树状数组的化，可以一个一个插入的构建
// 树状数组只能维护前缀“操作和”(前缀和，前缀积，前缀最大最小)
template<typename T>
struct BIT{
#ifndef lowbit
#define lowbit(x) (x & (-x));
#endif
    static const int maxn = 1e3+50;
    int n;
    T t[maxn];

    BIT<T> () {}
    BIT<T> (int _n): n(_n) { memset(t, 0, sizeof(t)); }
    BIT<T> (int _n, T *a): n(_n) {
        memset(t, 0, sizeof(t));
        /* 从 1 开始 */
        for (int i = 1; i <= n; ++ i){
            t[i] += a[i];
            int j = i + lowbit(i);
            if (j <= n) t[j] += t[i];
        }
    }

    void add(int i, T x){
        while (i <= n){
            t[i] += x;
            i += lowbit(i);
        }
    }

    /* 1-index */
    T sum(int i){
        T ans = 0;
        while (i > 0){
            ans += t[i];
            i -= lowbit(i);
        }
        return ans;
    }
    /* 1-index [l, r] */
    T sum(int i, int j){
        return sum(j) - sum(i - 1);
    }
/*
href: https://mingshan.fun/2019/11/29/binary-indexed-tree/
note:
    C[i] --> [i - lowbit(i) + 1, i]
    father of i --> i + lowbit(i)
    node number of i --> lowbit(i)
*/
};

// https://mingshan.fun/2019/11/29/binary-indexed-tree/
// https://www.cnblogs.com/Last--Whisper/p/13823614.html
// https://leetcode-cn.com/circle/article/OeMXPy/