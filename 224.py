class Solution:
    def calculate(self, s: str) -> int:
        OPStack = list()
        ValStack = list() 
        ValStack.append(0)
        l = len(s)
        for i in range(l):
            if s[i] == "(" or s[i]== ")" or s[i]==" ":
                continue
            elif s[i] == "+" or s[i] == "-":
                if not OPStack:
                    OPStack.append(s[i])
                else:
                    op = OPStack.pop()
                    OPStack.append(s[i])
                    temp = self.cal(op,ValStack[-2],ValStack[-1])
                    ValStack.pop()
                    ValStack.pop()
                    ValStack.append(temp)
            else:
                a = i+1
                while a < l and s[a]!="+" and s[a]!="-" and s[a]!=")"and s[a]!="(":
                    a += 1
                num = "".join(s[i:a])
                num = int(num)
                ValStack.append(num)
        if len(OPStack) == 1:
            op = OPStack[0]
            return self.cal(op,ValStack[-2],ValStack[-1])
        return ValStack[1]
    def cal(self,op,num1,num2):
        if op == "+":
            return num1+num2
        else:
            return num1-num2
s = Solution()
print(s.calculate("  -2+(1 + 2) "))
