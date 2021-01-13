class Solution:
    def convert_1(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        line = ["" for _ in range(numRows)]
        b = True
        count = 0
        num = 2*numRows-2
        for index, char in enumerate(s):
            remainder  = index % num 
            if b :
                line[remainder] +=char
                count += 1
                if count >= numRows and numRows>2:
                    b = False
            else:
                line[num -remainder] += char
                count += 1
                if count >= num:
                    count = 0
                    b = True

        return  "".join(line)

    def convert_2(self,s:str , numRows: int) -> str:
        if numRows ==1 :
            return s
        num = 2*numRows -2
        l = len(s)
        res = ""
        for i in range(0,numRows):
            for j in range(0,l-i,num):
                res += s[j+i]
                if(i != 0 and i != numRows-1 and j+num-i <n):
                    res +=s[j+num-i]
        return res
#更加简洁的方法
    def convert_3(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
        
s =Solution()
print (s.convert_2("ABC",2))