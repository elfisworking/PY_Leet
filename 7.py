# 整数反转
# https://leetcode-cn.com/problems/reverse-integer/
# this function spend 28ms 13MB
def reverse_1(x):
    """
    :type x: int
    :rtype: int
    """
    y = 0
    if x == y:
        return y
    elif  x > 0 :
        x= str(x)
        y = int(x[::-1])
    else:
        x = str(x)[1:]
        y = int("-"+x[::-1])
    if -2**31 < y < 2**31 -1:
        return y
    else:
        return 0 
# this function spend less time (12ms 13MB)
def reverse_2(x):
        """
        :type x: int
        :rtype: int
        """
        listX = str(x).split('-')           # 把数字转字符串并对-分割，如果有- 则列表长度为2
        if len(listX) >1:                  
            x = int('-' + listX[-1][::-1])  # 反转并加上负号
        else:
            x = int(listX[-1][::-1])        # 反转
        if -2**31< x <2**31-1:
            return x
        else:
            return 0
def reverse_3(x):
    """
    :type x:int
    :rtype:int
    """
    sum = 0
    temp = x
    x= abs(x)
    while x :
        sum = sum * 10 + x % 10
        x= int(x / 10)
    sum = sum if temp > 0 else -sum
    if -2**31 < sum < 2**31 -1 :   
        return sum
    else:
        return 0 
print(reverse_3(1563847412))

