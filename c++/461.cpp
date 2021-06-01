class Solution {
public:
    int hammingDistance(int x, int y) {
        int op  = x ^ y;
        int res = 0;
        while(op){
            op &= (op-1);
            res++;
        }
        return res;

    }
};