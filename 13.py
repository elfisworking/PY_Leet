# 13. 罗马数字转整数
# https://leetcode-cn.com/problems/roman-to-integer/
class Solution:
    # 状态转换机 模拟做法
    def romanToInt(self, s: str) -> int:
        # val = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        # symbol  = ["I","IV","V","IX","XL","L","XC","C","CD","D","CM"，"M"]
        l = len(s)
        i = res = 0
        while i < l:
            if i < l-1 and s[i]=="I" and s[i+1]=="V":
                i += 1
                res += 4
            elif i< l-1 and s[i]=="I" and s[i+1]=="X":
                i += 1
                res +=9
            elif s[i] == "I":
                res += 1
            elif s[i] == "V":
                res += 5
            elif i<l-1 and s[i] == "X" and s[i+1] == "L":
                i += 1
                res += 40
            elif i<l-1 and s[i] == "X" and s[i+1] == "C":
                i += 1
                res += 90
            elif s[i] == "X":
                res += 10
            elif s[i] == "L":
                res += 50
            elif i < l-1 and s[i] == "C" and s[i+1] == "D":
                i += 1
                res += 400
            elif i < l-1 and s[i] == "C" and s[i+1] == "M":
                i += 1
                res += 900
            elif s[i] == "C":
                res += 100
            elif s[i] == "D":
                res += 500
                print(i,res)
            elif s[i] == "M":
                res += 1000 
            i += 1
        return res