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
def reverse_2(self, x):
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
print(2**31 - 1)
print(reverse(1563847412))

