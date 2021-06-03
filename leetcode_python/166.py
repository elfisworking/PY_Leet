# 166. 分数到小数
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/
# 感觉不会做的样子
# 怎么判断无限不循环消失
# 模拟的方法 
class Solution:
    def fractionToDecimal(self,numerator,denominator):
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        numer = abs(numerator)
        denomin = abs(numerator)

        a, remind = divmod(numer,denomin)
        res.append(str(a))

        if remind == 0:
            return "".join(res)
        
        # 添加小数点
        res.append(".")
        dic = {}
        while remind != 0:
            if remind in dic:
                res.insert(dic[remind],"(")
                res.append(")")
                break
            dic[remind] = len(res) # 记录括号的位置
            remind *= 10 # 余数加0
            a , remind = divmod(remind,denomin)
            res.append(str(a))
        return "".join(res)