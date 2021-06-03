def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    len1 = len(l1)
    len2 = len(l2)
    carry = 0
    result = []
    if len1 <= len2:
        index = 0
        while index < len1:
            val1 = l1[index]
            val2 = l2[index]
            value = val2 + val1 + carry
            carry = int(value  / 10)
            result.append(value % 10)
            index += 1
        while index < len2:
            val2 = l2[index]
            value = val2 + carry
            carry = int(value / 10)
            result.append(value % 10)
            index += 1 
        if carry != 0:
            result.append(carry)
    else:
        index = 0
        while index < len2:
            val1 = l1[index]
            val2 = l2[index]
            value = val2 + val1 + carry
            carry = int(value  / 10)
            result.append(value % 10)
            index += 1
        while index < len1:
            val1 = l1[index]
            value = val1 + carry
            carry = int(value / 10)
            result.append(value % 10)
            index += 1 
        if carry != 0:
            result.append(carry)
    return result

reuslt = addTwoNumbers([2,4,3],[5,1])
print(reuslt)